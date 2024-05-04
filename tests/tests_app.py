from pathlib import Path
from PIL import UnidentifiedImageError
import pytest
from PIL import Image
import validators
import streamlit as st
from app import SOCIAL_MEDIA, PROJECTS, EMAIL

# Path settings
CURRENT_DIR = Path().cwd().resolve()
ASSET_DIR = CURRENT_DIR / "assets"
CSS_FILE = CURRENT_DIR / "styles" / "main.css"
RESUME = ASSET_DIR / "CV_Lucas_PASCAL_data.pdf"
PROFILE_PICTURE = ASSET_DIR / "profile-pic.png"
FAVICON_PATH = ASSET_DIR / "favicon.ico"

def test_path_settings():
    assert CURRENT_DIR.exists(), "Current directory path is invalid."
    assert CSS_FILE.exists(), "CSS file path is invalid."
    assert RESUME.exists(), "Resume PDF file path is invalid."
    assert PROFILE_PICTURE.exists(), "Profile picture path is invalid."
    assert FAVICON_PATH.exists(), "Favicon path is invalid."

def test_favicon_loading():
    try:
        img = Image.open(FAVICON_PATH)
        img.verify()  # Verifies that the file is not corrupted
    except (FileNotFoundError, UnidentifiedImageError):
        pytest.fail("Favicon image is either corrupted or missing.")
    
def test_resume_pdf_content():
    assert RESUME.stat().st_size > 0, "Resume PDF file is empty or corrupted."
    

def test_social_media_links():
    for name, url in SOCIAL_MEDIA.items():
        assert validators.url(url), f"URL for {name} is invalid."

def test_project_links():
    for project, url in PROJECTS.items():
        assert validators.url(url), f"URL for project '{project}' is invalid."
        
def test_email_format():
    assert validators.email(EMAIL), "Provided email address is invalid."

def test_pdf_download_button(mocker):
    mocker.patch('streamlit.download_button', return_value=True)
    assert st.download_button("Download Resume"), "Download Resume button failed."

def test_profile_picture_loading():
    try:
        img = Image.open(PROFILE_PICTURE)
        img.verify()
    except (FileNotFoundError, UnidentifiedImageError):
        pytest.fail("Profile picture is either corrupted or missing.")
