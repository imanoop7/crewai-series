from fastmcp import FastMCP

mcp = FastMCP("Research Tools")


@mcp.tool()
def format_blog_post(title: str, content: str, author: str = "", tags: str = "") -> str:
    """Format content as a blog post with metadata"""
    from datetime import datetime
    
    return f"""---
title: {title}
author: {author}
date: {datetime.now().strftime('%Y-%m-%d')}
tags: {tags}
---

# {title}

{content}

---
*Written by {author} on {datetime.now().strftime('%B %d, %Y')}*
"""

if __name__ == "__main__":
    mcp.run(transport="stdio")