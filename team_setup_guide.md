# Project Setup & Push Guide


---

## For Shehzad (UI Branch)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### Step 2: Switch to Your Branch
```bash
git checkout ui-shehzad
```

### Step 3: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Work on Your Tasks
- Make your changes to the code
- Test your work locally

### Step 6: Push Your Work
```bash
# Check what files you changed
git status

# Add all changes
git add .

# Commit with a message
git commit -m "Description of what you did"

# Push to your branch
git push origin ui-shehzad
```

### Daily Workflow (After First Setup)
```bash
# 1. Pull latest changes
git pull origin ui-shehzad

# 2. Activate virtual environment
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Mac/Linux

# 3. Work on your tasks

# 4. Push your work
git add .
git commit -m "Your message"
git push origin ui-shehzad
```

---

## Important Notes for Both Members

### ⚠️ Common Issues & Solutions

**1. If you get "branch not found" error:**
```bash
git fetch origin
git checkout mysql-saayid  # or ui-shehzad
```

**2. If you get merge conflicts:**
```bash
git pull origin mysql-saayid  # or ui-shehzad
# Fix conflicts in files
git add .
git commit -m "Resolved conflicts"
git push origin mysql-saayid  # or ui-shehzad
```

**3. If you need to undo changes:**
```bash
# Undo uncommitted changes
git checkout -- filename

# Undo last commit (keep changes)
git reset --soft HEAD~1
```

### 📝 Good Commit Message Examples
- ✅ "Added login functionality to homepage"
- ✅ "Fixed database connection issue"
- ✅ "Updated UI for dashboard page"
- ❌ "changes" (too vague)
- ❌ "asdfgh" (not descriptive)

### 🔄 Best Practices
1. **Pull before you start working** each day
2. **Commit frequently** with clear messages
3. **Push at the end of each work session**
4. **Test your code** before pushing
5. **Don't work on the main branch** - always use your assigned branch

### 🆘 Need Help?
If you get stuck, share:
- The command you ran
- The error message you got
- Screenshot if possible