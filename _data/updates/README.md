# Updates Data Format

Each update is stored as a JSON file in this folder. The filename should follow `YYYY-MM-DD.json` pattern (e.g., `2026-03-27.json`). Files are automatically loaded by Jekyll and displayed on the updates page in reverse chronological order.

## JSON Schema

```json
{
  "date": "Month DD, YYYY",
  "title": "Brief title of the update",
  "overview": "Brief overview in Chinese or English.",
  "categories": [
    {
      "title": "Category Title",
      "changes": [
        {
          "type": "added",        // optional: "added", "improvement", "fixed", "technical"
          "text": "Description of the change (markdown supported)"
        },
        {
          "text": "Plain change without type"
        }
      ]
    }
  ]
}
```

## Change Types

- `added`: New feature or addition (显示为“新增”)
- `improvement`: Enhancement or improvement (显示为“改进”)
- `fixed`: Bug fix (显示为“修复”)
- `technical`: Technical change (显示为“技术”)

If `type` is omitted, the change is displayed as plain text.

## Text Formatting

Use Markdown for formatting:
- `**bold**` for emphasis
- `` `code` `` for inline code
- `[link](url)` for links

Avoid HTML tags; use Markdown equivalents.

## Example

See `2026-03-27.json` for a complete example.

## Adding a New Update

1. Create a new JSON file with the current date (e.g., `2026-03-28.json`)
2. Follow the schema above
3. Commit and push to GitHub
4. GitHub Pages will rebuild the site automatically

No need to edit `updates.html` or any other file.