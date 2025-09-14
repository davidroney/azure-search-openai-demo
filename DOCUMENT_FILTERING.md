# Document Filtering by Subfolder Feature

This feature allows users to filter documents by their subfolder names in the developer settings. Documents are automatically tagged with metadata equal to their subfolder name during ingestion.

## How it works

1. **Automatic Category Detection**: When processing documents, the system automatically detects the subfolder name and assigns it as the document's category
2. **Dynamic Dropdown**: The Settings UI dynamically populates the "Include category" dropdown with available categories from the search index
3. **Filtering**: Users can select a category to filter search results to only include documents from that category

## Example

If you have documents organized like this:
```
data/
├── Json_Examples/
│   ├── file1.json
│   └── file2.json
├── Multimodal_Examples/
│   └── report.pdf
└── Benefits/
    └── handbook.pdf
```

After processing, the categories dropdown will show:
- All (default)
- Benefits
- Json_Examples  
- Multimodal_Examples

## Testing the Feature

1. **Ingest documents** with the standard prepdocs process. Documents in subfolders will automatically get categorized.

2. **Check categories API**: Visit `/categories` endpoint to see available categories:
   ```bash
   curl http://localhost:50505/categories
   ```

3. **Use the UI**: 
   - Open Chat or Ask page
   - Click the Settings button
   - Look for "Include category" dropdown
   - Select a category to filter results

4. **Verify filtering**: Ask questions and observe that only documents from the selected category are used in responses.

## Manual Category Override

You can still manually set categories using the `--category` parameter in prepdocs:
```bash
python prepdocs.py --category "CustomCategory" data/mydocs/*
```

This will override the automatic detection for those documents.

## API Endpoints

- `GET /categories` - Returns list of available categories from the search index
- `GET /config` - Existing endpoint, unchanged
- `POST /ask` and `POST /chat` - Existing endpoints, now respect the `include_category` filter

## Code Changes Summary

**Backend:**
- `filestrategy.py`: Auto-detects categories from file paths
- `app.py`: New `/categories` endpoint  
- `searchmanager.py`: Method to retrieve available categories

**Frontend:**
- `api.ts`: New `categoriesApi()` function
- `Settings.tsx`: Dynamic category dropdown
- `Chat.tsx` & `Ask.tsx`: Fetch and pass categories to Settings