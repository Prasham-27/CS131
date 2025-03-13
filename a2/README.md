# Organize Script

## What this script does

The `organize` command automatically sorts and organizes files in a specified directory (or current directory by default) into categorized subdirectories based on their file types/extensions.

## Why/When this command is useful

- Useful when your Downloads or Desktop folders become cluttered with files of various types.
- Quickly organizes files into logical groups, making it easier to find and manage your files.
- Saves time by automating manual sorting tasks.
- Helps maintain a clean digital workspace by categorizing files by their purpose.

## How you can use this command

### Installation

#### Method 1: Make it available in the current directory only

Make sure the script is executable:

```
chmod +x organize
```

Then execute it directly from its location:

```
./organize [optional-directory-path]
```

#### Method 2: Make it available system-wide (Linux/Mac)

1. Copy the script to a directory in your PATH:

   **For Linux:**
   ```
   sudo cp organize /usr/local/bin/
   sudo chmod +x /usr/local/bin/organize
   ```

   **For Mac:**
   ```
   sudo cp organize /usr/local/bin/
   sudo chmod +x /usr/local/bin/organize
   ```

   **Alternative (no sudo required):**
   ```
   mkdir -p ~/bin
   cp organize ~/bin/
   chmod +x ~/bin/organize
   echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc  # or ~/.zshrc for Mac
   source ~/.bashrc  # or source ~/.zshrc for Mac
   ```

2. Now you can run the command from any directory:
   ```
   organize [optional-directory-path]
   ```

### Usage Syntax:

```
organize [directory-path]
```

- If no argument is provided, the script organizes files in the current directory.
- If a path is provided, the script organizes files in that specified directory.

### File Categories

The script organizes files into the following categories:

- **Images**: jpg, jpeg, png, gif, bmp
- **Videos**: mp4, mkv, avi, mov
- **Audio**: mp3, wav, aac, flac
- **Documents**: pdf, doc, docx, txt, ppt, pptx
- **Archives**: zip, tar, gz, rar
- **Code**: sh, py, java, c, cpp, js, html, php, css
- **Subtitles**: ass, srt, sub, vtt
- **Ebooks**: epub, mobi, azw, azw3
- **Fonts**: ttf, otf, woff, woff2
- **Others**: Any other file types

### Behavior with Existing Directories

- If a category directory (like "Images" or "Documents") already exists, the script will use that existing directory and add files to it.
- The script will not overwrite or delete existing files in the destination directories.
- If a file with the same name already exists in the destination directory, the script will not move the file (standard behavior of the `mv` command).
- The script only processes files in the top level of the specified directory; it does not recursively organize files in subdirectories.
- Directories themselves are not moved or reorganized, only individual files.

## Examples

### Example 1: Organize current directory

```
~/Downloads$ organize
Files organized successfully in /home/user/Downloads.
```

**Before running command:**

```
Downloads/
├── song.mp3
├── movie.mp4
├── document.pdf
├── image.png
├── archive.zip
├── book.epub
├── subtitle.srt
└── custom-font.ttf
```

**After running command:**

```
Downloads/
├── Audio/
│   └── song.mp3
├── Videos/
│   └── movie.mp4
├── Documents/
│   └── document.pdf
├── Images/
│   └── image.png
├── Archives/
│   └── archive.zip
├── Ebooks/
│   └── book.epub
├── Subtitles/
│   └── subtitle.srt
└── Fonts/
    └── custom-font.ttf
```

### Example 2: Organize specified directory

```
~$ organize ~/Desktop/test_folder/
Files organized successfully in /home/user/Desktop/test_folder.
```

**Resulting structure:**

```
test_folder/
├── Code/
│   ├── script.sh
│   └── program.py
├── Documents/
│   ├── notes.txt
│   └── slides.pptx
├── Ebooks/
│   ├── novel.epub
│   └── textbook.pdf
├── Subtitles/
│   └── movie-subtitles.srt
└── Others/
    └── unknownfile.xyz
```

### Example 3: Real-world usage from any directory

```
# You can be in any directory
~$ cd /some/random/path

# And organize your Downloads folder
/some/random/path$ organize ~/Downloads
Files organized successfully in /home/user/Downloads.

# Or organize your current working directory
/some/random/path$ organize
Files organized successfully in /some/random/path.
```

### Example 4: Behavior with existing directories

**Before:**
```
Downloads/
├── Images/           # Existing directory with some files
│   ├── vacation.jpg
│   └── profile.png
├── new-photo.jpg     # New file to be organized
└── screenshot.png    # New file to be organized
```

**After running `organize`:**
```
Downloads/
├── Images/           # Existing directory used by the script
│   ├── vacation.jpg  # Existing files remain untouched
│   ├── profile.png   # Existing files remain untouched
│   ├── new-photo.jpg # New file moved here
│   └── screenshot.png # New file moved here
```

---
