#!/usr/bin/env python3
"""
Simple test to verify category extraction from file paths.
"""
import sys
import os

# Add the backend directory to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app', 'backend'))

from prepdocslib.filestrategy import extract_category_from_path


def test_category_extraction():
    """Test the extract_category_from_path function."""
    
    test_cases = [
        # Test case: (file_path, expected_category)
        ("data/Json_Examples/file.json", "Json_Examples"),
        ("data/Multimodal_Examples/report.pdf", "Multimodal_Examples"),
        ("data/Benefits/handbook.pdf", "Benefits"),
        ("/absolute/path/data/Json_Examples/nested/file.txt", "Json_Examples"),
        ("./data/Json_Examples/file.json", "Json_Examples"),
        ("Json_Examples/file.json", "Json_Examples"),
        ("data/file.json", "data"),  # File directly in data folder
        ("file.json", None),  # File with no directory
        ("", None),  # Empty path
    ]
    
    print("Testing category extraction...")
    
    for file_path, expected in test_cases:
        result = extract_category_from_path(file_path)
        status = "✓" if result == expected else "✗"
        print(f"{status} Path: '{file_path}' -> Category: '{result}' (expected: '{expected}')")
        
        if result != expected:
            print(f"  FAILED: Expected '{expected}', got '{result}'")
    
    print("\nDone!")


if __name__ == "__main__":
    test_category_extraction()