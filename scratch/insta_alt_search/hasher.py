import imagehash
from PIL import Image
from io import BytesIO
import requests


def compute_phash(source) -> str:
    """Compute perceptual hash from a file path, URL, or file-like object.
    
    Returns a 16-character hex string representing the 64-bit pHash.
    """
    if isinstance(source, str) and source.startswith(("http://", "https://")):
        resp = requests.get(source, timeout=15)
        resp.raise_for_status()
        img = Image.open(BytesIO(resp.content))
    elif isinstance(source, (str,)):
        img = Image.open(source)
    else:
        img = Image.open(source)

    return str(imagehash.phash(img))


def hamming_distance(hash1: str, hash2: str) -> int:
    """Return bit-level difference between two hex hash strings.
    
    0 = identical, ≤10 = very likely same image, >20 = different images.
    """
    return imagehash.hex_to_hash(hash1) - imagehash.hex_to_hash(hash2)


if __name__ == "__main__":
    # Self-check: two identical hashes should have distance 0
    h = compute_phash(Image.new("RGB", (100, 100), color="red"))
    assert hamming_distance(h, h) == 0
    print(f"Self-check passed. Sample hash: {h}")
