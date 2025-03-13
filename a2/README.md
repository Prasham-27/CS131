# Organize Command

## What this command does

The `organize` command automatically sorts and organizes files in a specified directory (or current directory by default) into categorized subdirectories based on their file types/extensions.

## Why/When this command is useful

- Useful when your Downloads or Desktop folders become cluttered with files of various types.
- Quickly organizes files into logical groups, making it easier to find and manage your files.
- Saves time by automating manual sorting tasks.
- Helps maintain a clean digital workspace by categorizing files by their purpose.

## How you can use this command

### Installation

Make sure the script is executable:

```
chmod +x organize
```

Then place it in your PATH or execute directly from its location:

```
./organize [optional-directory-path]
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
- **Code**: sh, py, java, c, cpp, js, html, css
- **Subtitles**: srt, sub, vtt
- **Ebooks**: epub, mobi, azw, azw3
- **Fonts**: ttf, otf, woff, woff2
- **Others**: Any other file types

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

### Example 3: Real-world usage

```
~$ cd ~/Downloads
~/Downloads$ ls
assignment.pdf  background.png  lecture.mp4  novel.epub  project.zip  subtitles.srt  theme.ttf

~/Downloads$ organize
Files organized successfully in /home/user/Downloads.

~/Downloads$ ls
Archives  Documents  Ebooks  Fonts  Images  Subtitles  Videos

~/Downloads$ find . -type f
./Archives/project.zip
./Documents/assignment.pdf
./Ebooks/novel.epub
./Fonts/theme.ttf
./Images/background.png
./Subtitles/subtitles.srt
./Videos/lecture.mp4
```

---
Answer from Perplexity: pplx.ai/share
