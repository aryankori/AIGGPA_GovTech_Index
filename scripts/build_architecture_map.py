import os
import json

def get_dir_structure(rootdir):
    ignore_dirs = {'.git', 'node_modules', '__pycache__', '.vscode', '.agents', '.tmp.drivedownload', '.tmp.driveupload'}
    
    def format_size(size):
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
            
    def recurse(path):
        name = os.path.basename(path)
        if name in ignore_dirs:
            return None
            
        if os.path.isdir(path):
            children = []
            total_size = 0
            for item in sorted(os.listdir(path)):
                item_path = os.path.join(path, item)
                child = recurse(item_path)
                if child:
                    children.append(child)
                    total_size += child.get('size_bytes', 0)
            
            return {
                'name': name,
                'type': 'directory',
                'size_bytes': total_size,
                'size': format_size(total_size),
                'children': children
            }
        else:
            size = os.path.getsize(path)
            ext = os.path.splitext(name)[1].lower()
            return {
                'name': name,
                'type': 'file',
                'extension': ext,
                'size_bytes': size,
                'size': format_size(size)
            }
            
    root_node = recurse(rootdir)
    root_node['name'] = 'AIGGPA_Report' # Overwrite '.'
    return root_node

def build_html(json_data):
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AIGGPA Project Architecture</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --bg-color: #0f172a;
            --glass-bg: rgba(30, 41, 59, 0.7);
            --glass-border: rgba(255, 255, 255, 0.1);
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --accent: #3b82f6;
            --folder-color: #fbbf24;
        }
        body {
            margin: 0;
            padding: 2rem;
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, var(--bg-color), #020617);
            color: var(--text-main);
            min-height: 100vh;
        }
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: var(--glass-bg);
            backdrop-filter: blur(10px);
            border: 1px solid var(--glass-border);
            border-radius: 16px;
            padding: 2rem;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        }
        h1 {
            font-weight: 600;
            margin-top: 0;
            border-bottom: 1px solid var(--glass-border);
            padding-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .search-bar {
            width: 100%;
            padding: 12px 20px;
            margin-bottom: 2rem;
            background: rgba(0,0,0,0.2);
            border: 1px solid var(--glass-border);
            border-radius: 8px;
            color: white;
            font-size: 1rem;
            outline: none;
            transition: border-color 0.3s;
        }
        .search-bar:focus {
            border-color: var(--accent);
        }
        ul {
            list-style-type: none;
            padding-left: 20px;
        }
        .tree-root {
            padding-left: 0;
        }
        li {
            margin: 6px 0;
            position: relative;
        }
        .node {
            display: flex;
            align-items: center;
            padding: 6px 10px;
            border-radius: 6px;
            cursor: pointer;
            transition: background 0.2s;
        }
        .node:hover {
            background: rgba(255, 255, 255, 0.05);
        }
        .icon {
            width: 24px;
            text-align: center;
            margin-right: 10px;
            font-size: 1.1rem;
        }
        .folder-icon { color: var(--folder-color); }
        .file-icon { color: var(--text-muted); }
        .file-icon.py { color: #3b82f6; }
        .file-icon.json { color: #10b981; }
        .file-icon.pdf { color: #ef4444; }
        .file-icon.md { color: #8b5cf6; }
        .file-icon.tex { color: #14b8a6; }
        .file-icon.html { color: #f97316; }
        .name { flex-grow: 1; font-weight: 400; }
        .size {
            font-size: 0.8rem;
            color: var(--text-muted);
            background: rgba(0,0,0,0.3);
            padding: 2px 8px;
            border-radius: 12px;
        }
        .children {
            display: none;
            border-left: 1px dashed var(--glass-border);
            margin-left: 11px;
        }
        .open > .children {
            display: block;
            animation: slideDown 0.3s ease;
        }
        .open > .node > .folder-icon:before {
            content: "\\f07c"; /* open folder icon */
        }
        @keyframes slideDown {
            from { opacity: 0; transform: translateY(-5px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1><i class="fa-solid fa-sitemap" style="color: var(--accent);"></i> Project Architecture</h1>
        <input type="text" id="searchInput" class="search-bar" placeholder="Search files and folders...">
        <ul id="tree" class="tree-root"></ul>
    </div>

    <script>
        const treeData = __JSON_DATA__;

        function getFileIconClass(ext) {
            ext = ext.replace('.', '').toLowerCase();
            const map = {
                'py': 'fa-brands fa-python py',
                'json': 'fa-solid fa-code json',
                'pdf': 'fa-solid fa-file-pdf pdf',
                'md': 'fa-brands fa-markdown md',
                'tex': 'fa-solid fa-file-code tex',
                'html': 'fa-brands fa-html5 html',
                'txt': 'fa-solid fa-file-lines',
                'csv': 'fa-solid fa-file-csv',
                'xlsx': 'fa-solid fa-file-excel json',
                'docx': 'fa-solid fa-file-word py'
            };
            return map[ext] || 'fa-solid fa-file';
        }

        function createNodeHtml(node) {
            const isDir = node.type === 'directory';
            const iconClass = isDir ? 'fa-solid fa-folder folder-icon' : getFileIconClass(node.extension) + ' file-icon';
            
            let html = `<li class="${isDir ? 'folder' : 'file'}">`;
            html += `<div class="node" onclick="${isDir ? 'this.parentElement.classList.toggle(\\'open\\')' : ''}">`;
            html += `<i class="${iconClass} icon"></i>`;
            html += `<span class="name">${node.name}</span>`;
            if (node.size) {
                html += `<span class="size">${node.size}</span>`;
            }
            html += `</div>`;

            if (isDir && node.children) {
                html += `<ul class="children">`;
                node.children.forEach(child => {
                    html += createNodeHtml(child);
                });
                html += `</ul>`;
            }
            html += `</li>`;
            return html;
        }

        document.getElementById('tree').innerHTML = createNodeHtml(treeData);
        // Open root by default
        document.querySelector('.tree-root > li').classList.add('open');

        // Simple search functionality
        document.getElementById('searchInput').addEventListener('input', function(e) {
            const term = e.target.value.toLowerCase();
            const nodes = document.querySelectorAll('.node');
            
            nodes.forEach(node => {
                const name = node.querySelector('.name').innerText.toLowerCase();
                const parentLi = node.parentElement;
                
                if (name.includes(term)) {
                    node.style.display = 'flex';
                    // Ensure parents are visible and open
                    let current = parentLi.parentElement;
                    while(current && current.classList.contains('children')) {
                        current.parentElement.classList.add('open');
                        current.parentElement.querySelector('.node').style.display = 'flex';
                        current = current.parentElement.parentElement;
                    }
                } else if (term !== '') {
                    // Only hide files or empty folders if searching
                    if(parentLi.classList.contains('file')) {
                        node.style.display = 'none';
                    }
                } else {
                    node.style.display = 'flex';
                }
            });
        });
    </script>
</body>
</html>"""
    
    # Inject JSON data into template
    json_str = json.dumps(json_data)
    final_html = html_template.replace('__JSON_DATA__', json_str)
    
    with open('project_architecture.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

if __name__ == '__main__':
    print("Scanning directory structure...")
    data = get_dir_structure('.')
    
    print("Writing project_architecture.json...")
    with open('project_architecture.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
        
    print("Building project_architecture.html...")
    build_html(data)
    print("Done! Architecture mapping complete.")
