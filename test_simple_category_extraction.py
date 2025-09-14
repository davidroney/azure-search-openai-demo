#!/usr/bin/env python3
"""
Simple test to verify category extraction from file paths.
"""
import os

def extract_category_from_path(file_path: str, base_path: str = None) -> str:
    """
    Extract category from file path based on subfolder name.
    
    Args:
        file_path: Full path to the file
        base_path: Optional base path to remove from file_path
    
    Returns:
        Category name (subfolder name) or None if no subfolder detected
    """
    try:
        # Normalize the path
        path = os.path.normpath(file_path)
        
        # Get the directory containing the file
        dir_path = os.path.dirname(path)
        
        # If base_path is provided, make path relative to it
        if base_path and dir_path.startswith(base_path):
            dir_path = os.path.relpath(dir_path, base_path)
        
        # Split the path into parts
        path_parts = dir_path.split(os.sep)
        
        # Filter out empty parts and current directory references
        path_parts = [part for part in path_parts if part and part != '.' and part != '..' and part != '']
        
        # Return the first non-empty directory as the category
        if path_parts:
            return path_parts[0]
        
        return None
    except Exception as e:
        print(f"Could not extract category from path {file_path}: {e}")
        return None


def test_category_extraction():
    """Test the extract_category_from_path function."""
    
    test_cases = [
        # Test case: (file_path, expected_category)
        ("data/Json_Examples/file.json", "data"),
        ("Json_Examples/file.json", "Json_Examples"),
        ("Multimodal_Examples/report.pdf", "Multimodal_Examples"),
        ("Benefits/handbook.pdf", "Benefits"),
        ("/absolute/path/data/Json_Examples/nested/file.txt", "data"),
        ("./Json_Examples/file.json", "Json_Examples"),
        ("subdir/Json_Examples/file.json", "subdir"),
        ("file.json", None),  # File with no directory
        ("", None),  # Empty path
    ]
    
    print("Testing category extraction...")
    
    all_passed = True
    for file_path, expected in test_cases:
        result = extract_category_from_path(file_path)
        status = "✓" if result == expected else "✗"
        print(f"{status} Path: '{file_path}' -> Category: '{result}' (expected: '{expected}')")
        
        if result != expected:
            print(f"  FAILED: Expected '{expected}', got '{result}'")
            all_passed = False
    
    print(f"\nTest results: {'All tests passed!' if all_passed else 'Some tests failed!'}")
    return all_passed


if __name__ == "__main__":
    test_category_extraction()