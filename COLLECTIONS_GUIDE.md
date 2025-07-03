# PMM Collections Guide

## What Collections Will PMM Create?

After running PMM, you'll see new collections appear in your Plex libraries automatically based on your content.

### 🎬 **Movie Collections Examples**

#### **Decade Collections**
- **1980s Movies** (if you have 5+ movies from the 80s)
- **1990s Movies** (if you have 5+ movies from the 90s)  
- **2000s Movies** (if you have 5+ movies from the 2000s)
- **2010s Movies** (if you have 5+ movies from the 2010s)

#### **Genre Collections**
- **Action Movies** (if you have 10+ action movies)
- **Comedy Movies** (if you have 10+ comedies)
- **Horror Movies** (if you have 10+ horror movies)
- **Drama Movies** (if you have 10+ dramas)
- **Sci-Fi Movies** (if you have 10+ sci-fi movies)

#### **Studio Collections**
- **Disney Movies** (if you have 5+ Disney movies)
- **Warner Bros Movies** (if you have 5+ Warner Bros movies)
- **Universal Movies** (if you have 5+ Universal movies)

#### **Rating Collections**
- **Highly Rated Movies** (movies with 8.0+ rating, minimum 5 movies)

### 📺 **TV Show Collections Examples**

#### **Network Collections**
- **HBO Shows** (if you have 3+ HBO shows)
- **Netflix Shows** (if you have 3+ Netflix shows)
- **CBS Shows** (if you have 3+ CBS shows)
- **BBC Shows** (if you have 3+ BBC shows)

#### **Genre Collections**
- **Comedy TV Shows** (if you have 5+ comedy shows)
- **Drama TV Shows** (if you have 5+ drama shows)
- **Crime TV Shows** (if you have 5+ crime shows)

## How Collections Appear in Plex

### **Before PMM:**
```
Movies Library:
├── The Dark Knight (2008)
├── Inception (2010)
├── Interstellar (2014)
├── Top Gun (1986)
├── Die Hard (1988)
└── (individual movies listed)
```

### **After PMM:**
```
Movies Library:
├── 🎬 Collections
│   ├── 1980s Movies (3 items)
│   ├── 2000s Movies (2 items) 
│   ├── 2010s Movies (2 items)
│   ├── Action Movies (4 items)
│   └── Highly Rated Movies (3 items)
└── 🎭 Individual Movies
    ├── The Dark Knight (2008)
    ├── Inception (2010)
    ├── Interstellar (2014)
    ├── Top Gun (1986)
    └── Die Hard (1988)
```

## Collection Benefits

### **Better Organization**
- **Browse by decade** - "Show me 90s movies"
- **Browse by genre** - "Show me all action movies"
- **Browse by studio** - "Show me all Disney movies"

### **Discovery**
- **Find forgotten movies** in your collection
- **See patterns** in your viewing preferences
- **Easily recommend** movies to family/friends

### **Visual Appeal**
- **Clean library presentation**
- **Professional look** like streaming services
- **Grouped similar content**

## Customization Options

### **Minimum Items**
Control when collections are created:
```yaml
collections:
  movies:
    decades:
      minimum_items: 5  # Only create if 5+ movies
    genres:
      minimum_items: 10 # Only create if 10+ movies
```

### **Enable/Disable Types**
Turn collection types on/off:
```yaml
collections:
  movies:
    decades:
      enabled: true   # Create decade collections
    genres:
      enabled: true   # Create genre collections
    studios:
      enabled: false  # Don't create studio collections
```

### **Rating Thresholds**
Customize what counts as "highly rated":
```yaml
collections:
  movies:
    ratings:
      highly_rated_threshold: 8.0  # 8.0+ is "highly rated"
      minimum_items: 5
```

## What You'll See in Plex

1. **Collections Tab** - New section in your library
2. **Smart Organization** - Content automatically grouped
3. **Professional Look** - Like Netflix/Disney+ collections
4. **Easy Browsing** - Find content by type, decade, genre
5. **Updated Automatically** - New content added to appropriate collections

## Collection Updates

- **Automatic** - PMM updates collections when it runs
- **New Content** - Added to appropriate existing collections
- **Smart Logic** - Only creates collections with enough content
- **No Duplicates** - Movies appear in individual library AND collections

Collections make your Plex library look and feel like a professional streaming service! 🎬✨
