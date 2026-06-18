import os
import subprocess
import json
import tempfile

image_dir = r"C:\Users\aryan\Downloads\Photos-3-001"
image_files = [
    "IMG20260618112741.jpg",
    "IMG20260618112748.jpg",
    "IMG20260618112802.jpg",
    "IMG20260618112854.jpg",
    "IMG20260618112737.jpg",
    "IMG20260618112753.jpg",
    "IMG20260618112504.jpg",
    "IMG20260618112725.jpg"
]

ps_script_content = """
param([string]$ImagePath)

[void][System.Reflection.Assembly]::LoadWithPartialName("System.Runtime.WindowsRuntime")
[void][Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics.Imaging, ContentType = WindowsRuntime]
[void][Windows.Media.Ocr.OcrEngine, Windows.Media.Ocr, ContentType = WindowsRuntime]
[void][Windows.Storage.StorageFile, Windows.Storage, ContentType = WindowsRuntime]
[void][Windows.Storage.Streams.IRandomAccessStream, Windows.Storage, ContentType = WindowsRuntime]

function Get-WinRTResult {
    param($asyncOp, $resultType)
    $extType = [System.WindowsRuntimeSystemExtensions]
    $methods = $extType.GetMethods() | Where-Object { $_.Name -eq 'GetAwaiter' -and $_.IsGenericMethod }
    $method = $methods | Where-Object { 
        $params = $_.GetParameters()
        $params.Length -eq 1 -and 
        $_.GetGenericArguments().Length -eq 1 -and 
        $params[0].ParameterType.Name -like "*IAsyncOperation*"
    }
    $genericMethod = $method.MakeGenericMethod($resultType)
    $awaiter = $genericMethod.Invoke($null, @($asyncOp))
    return $awaiter.GetType().GetMethod('GetResult').Invoke($awaiter, $null)
}

try {
    $asyncOp = [Windows.Storage.StorageFile]::GetFileFromPathAsync($ImagePath)
    $file = Get-WinRTResult $asyncOp ([Windows.Storage.StorageFile])

    $asyncOp2 = $file.OpenAsync([Windows.Storage.FileAccessMode]::Read)
    $stream = Get-WinRTResult $asyncOp2 ([Windows.Storage.Streams.IRandomAccessStream])

    $asyncOp3 = [Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)
    $decoder = Get-WinRTResult $asyncOp3 ([Windows.Graphics.Imaging.BitmapDecoder])

    $asyncOp4 = $decoder.GetSoftwareBitmapAsync()
    $bitmap = Get-WinRTResult $asyncOp4 ([Windows.Graphics.Imaging.SoftwareBitmap])

    $engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
    if ($engine) {
        $asyncOp5 = $engine.RecognizeAsync($bitmap)
        $result = Get-WinRTResult $asyncOp5 ([Windows.Media.Ocr.OcrResult])
        Write-Output $result.Text
    } else {
        Write-Output "Error: Could not create OCR engine."
    }
} catch {
    Write-Output "Error occurred: $_"
    Write-Output $_.ScriptStackTrace
}
"""

# Write to temp .ps1 file
ps_script_path = os.path.join(tempfile.gettempdir(), "ocr_run.ps1")
with open(ps_script_path, "w", encoding="utf-8") as f:
    f.write(ps_script_content)

results = {}

for img in image_files:
    img_path = os.path.join(image_dir, img)
    if not os.path.exists(img_path):
        print(f"[-] File not found: {img_path}")
        continue
        
    print(f"[+] Processing OCR for: {img}...")
    
    try:
        proc = subprocess.Popen(
            ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", ps_script_path, img_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'
        )
        stdout, stderr = proc.communicate(timeout=20)
        
        extracted_text = stdout.strip()
        results[img] = extracted_text
        print(f"  [✓] Extracted ({len(extracted_text)} chars): {extracted_text[:100]}...")
        if stderr.strip():
            print(f"  [!] Stderr: {stderr.strip()}")
    except Exception as e:
        print(f"  [x] Error running OCR on {img}: {e}")

try:
    os.remove(ps_script_path)
except:
    pass

output_json = os.path.join(image_dir, "ocr_results.json")
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4, ensure_ascii=False)

print(f"\n[✓] OCR complete! Saved to {output_json}")
