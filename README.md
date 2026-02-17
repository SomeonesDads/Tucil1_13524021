# Queens Placement Solver

A Python-based solver for the Queens placement puzzle with real-time visualization capabilities. The program finds all valid configurations where queens must be placed on a colored board following specific constraints.

## Problem Description

Given an N×N board with N different colors, place one queen on each color such that:
- No two queens share the same row or column
- No two queens are within a radius of 1 from each other (including diagonals)

## Requirements

```bash
pip install pillow
```

**Dependencies:**
- Python 3.x
- tkinter (usually included with Python)
- Pillow (PIL) for image export

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install pillow
   ```
3. Run the program:
   ```bash
   python src/tucil1.py
   ```

## Usage

### Basic Workflow

1. **Launch the Program**
   ```bash
   python src/tucil1.py
   ```

2. **Load a Puzzle File**
   - Click "Choose File"
   - Select a `.txt` file containing the board configuration

3. **Configure Visualization (Optional)**
   - Check "Enable Live Visualization" to see the algorithm in action
   - Adjust the speed slider to control update rate
   - Lower values = faster, Higher values = slower

4. **Solve the Puzzle**
   - The program automatically starts solving after loading a file
   - Watch the iteration count and solutions found in the output panel

5. **Review Solutions**
   - Use "Next Solution" to browse through all valid solutions
   - Click "Save Results" to export solutions as text
   - Click "Export Images" to save all solutions as a composite image

### Input File Format

The input file should be an N×N grid where each character represents a color:

```
AAAA
BBBB
CCCC
DDDD
```

**Requirements:**
- Must be a square grid (N×N)
- Must have exactly N different colors
- Each color should appear on the board

### Example Test File

A sample test file (`1.txt`) is included:
```
AAAA
BBBB
CCCC
DDDD
```

This 4×4 puzzle is ideal for testing the visualization feature.

## UI Controls

### Main Controls
- **Choose File**: Load a puzzle file
- **Next Solution**: Navigate through found solutions
- **Save Results**: Export solutions to a text file
- **Export Images**: Save all solutions as a composite image (PNG/JPG)

### Visualization Controls
- **Enable Live Visualization**: Checkbox to toggle real-time visualization
- **Visualization Speed Slider**: Adjust delay between updates (1-100ms)

## Project Structure

```
Tucil1_13524021/
├── src/
│   └── tucil1.py          # Main program
├── test/
│   └── test_small.txt     # Sample test file
├── doc/                   # Documentation
├── bin/                   # Binaries (if any)
└── README.md             # This file
```

## Author Natanael I. Manurung (13524021)

Tucil1_13524021
