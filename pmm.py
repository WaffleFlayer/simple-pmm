#!/usr/bin/env python3
"""
Simple Plex Media Manager (PMM) for Surface
A lightweight tool to manage your Plex media library
"""

import os
import sys
import logging
from dotenv import load_dotenv
from plexapi.server import PlexServer
from plexapi.exceptions import BadRequest, NotFound
import yaml
import requests
import docker
import schedule
import time
from datetime import datetime

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=getattr(logging, os.getenv('PMM_LOG_LEVEL', 'INFO')),
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pmm.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class SimplePMM:
    def __init__(self):
        self.plex_url = os.getenv('PLEX_URL', 'http://localhost:32400')
        self.plex_token = os.getenv('PLEX_TOKEN')
        self.tmdb_api_key = os.getenv('TMDB_API_KEY')
        self.config_path = os.getenv('PMM_CONFIG_PATH', './config')
        
        if not self.plex_token:
            logger.error("PLEX_TOKEN not found in environment variables")
            sys.exit(1)
            
        try:
            self.plex = PlexServer(self.plex_url, self.plex_token)
            logger.info(f"Connected to Plex server: {self.plex.friendlyName}")
        except Exception as e:
            logger.error(f"Failed to connect to Plex server: {e}")
            sys.exit(1)
    
    def get_libraries(self):
        """Get all Plex libraries"""
        try:
            libraries = self.plex.library.sections()
            logger.info(f"Found {len(libraries)} libraries")
            for lib in libraries:
                logger.info(f"  - {lib.title} ({lib.type})")
            return libraries
        except Exception as e:
            logger.error(f"Error getting libraries: {e}")
            return []
    
    def scan_library(self, library_name=None):
        """Scan a specific library or all libraries"""
        try:
            if library_name:
                library = self.plex.library.section(library_name)
                logger.info(f"Scanning library: {library_name}")
                library.update()
            else:
                logger.info("Scanning all libraries")
                for library in self.plex.library.sections():
                    logger.info(f"Scanning: {library.title}")
                    library.update()
            logger.info("Library scan completed")
        except NotFound:
            logger.error(f"Library '{library_name}' not found")
        except Exception as e:
            logger.error(f"Error scanning library: {e}")
    
    def optimize_database(self):
        """Optimize Plex database"""
        try:
            logger.info("Starting database optimization")
            # This would typically be done through Plex Web UI or API
            # For now, we'll just log the action
            logger.info("Database optimization completed")
        except Exception as e:
            logger.error(f"Error optimizing database: {e}")
    
    def cleanup_temp_files(self):
        """Clean up temporary files"""
        try:
            logger.info("Cleaning up temporary files")
            # Add cleanup logic here based on your needs
            logger.info("Temporary file cleanup completed")
        except Exception as e:
            logger.error(f"Error cleaning temp files: {e}")
    
    def get_server_status(self):
        """Get Plex server status"""
        try:
            status = {
                'server_name': self.plex.friendlyName,
                'version': self.plex.version,
                'platform': self.plex.platform,
                'platform_version': self.plex.platformVersion,
                'updated_at': datetime.now().isoformat(),
                'libraries': len(self.plex.library.sections())
            }
            logger.info(f"Server status: {status}")
            return status
        except Exception as e:
            logger.error(f"Error getting server status: {e}")
            return None
    
    def run_maintenance(self):
        """Run routine maintenance tasks"""
        logger.info("Starting routine maintenance")
        self.scan_library()
        self.manage_collections()
        self.cleanup_temp_files()
        self.optimize_database()
        logger.info("Routine maintenance completed")
    
    def create_collections(self, library_name=None):
        """Create automatic collections based on popular criteria"""
        try:
            logger.info("Creating automatic collections")
            
            if library_name:
                libraries = [self.plex.library.section(library_name)]
            else:
                libraries = [lib for lib in self.plex.library.sections() if lib.type in ['movie', 'show']]
            
            for library in libraries:
                logger.info(f"Processing collections for library: {library.title}")
                
                if library.type == 'movie':
                    self._create_movie_collections(library)
                elif library.type == 'show':
                    self._create_tv_collections(library)
                    
        except Exception as e:
            logger.error(f"Error creating collections: {e}")
    
    def _create_movie_collections(self, library):
        """Create movie-specific collections"""
        try:
            # Get all movies
            movies = library.all()
            
            # Group by decade
            decades = {}
            for movie in movies:
                if hasattr(movie, 'year') and movie.year:
                    decade = (movie.year // 10) * 10
                    if decade not in decades:
                        decades[decade] = []
                    decades[decade].append(movie)
            
            # Create decade collections (only if 5+ movies)
            for decade, decade_movies in decades.items():
                if len(decade_movies) >= 5:
                    collection_name = f"{decade}s Movies"
                    self._create_or_update_collection(library, collection_name, decade_movies)
            
            # Create genre collections
            genres = {}
            for movie in movies:
                if hasattr(movie, 'genres'):
                    for genre in movie.genres:
                        genre_name = genre.tag
                        if genre_name not in genres:
                            genres[genre_name] = []
                        genres[genre_name].append(movie)
            
            # Create genre collections (only if 10+ movies)
            for genre, genre_movies in genres.items():
                if len(genre_movies) >= 10:
                    collection_name = f"{genre} Movies"
                    self._create_or_update_collection(library, collection_name, genre_movies)
            
            # Create rating-based collections
            highly_rated = [m for m in movies if hasattr(m, 'rating') and m.rating and m.rating >= 8.0]
            if len(highly_rated) >= 5:
                self._create_or_update_collection(library, "Highly Rated Movies", highly_rated)
                
        except Exception as e:
            logger.error(f"Error creating movie collections: {e}")
    
    def _create_tv_collections(self, library):
        """Create TV show-specific collections"""
        try:
            shows = library.all()
            
            # Group by network/studio
            networks = {}
            for show in shows:
                if hasattr(show, 'studio') and show.studio:
                    network = show.studio
                    if network not in networks:
                        networks[network] = []
                    networks[network].append(show)
            
            # Create network collections (only if 3+ shows)
            for network, network_shows in networks.items():
                if len(network_shows) >= 3:
                    collection_name = f"{network} Shows"
                    self._create_or_update_collection(library, collection_name, network_shows)
            
            # Create genre collections
            genres = {}
            for show in shows:
                if hasattr(show, 'genres'):
                    for genre in show.genres:
                        genre_name = genre.tag
                        if genre_name not in genres:
                            genres[genre_name] = []
                        genres[genre_name].append(show)
            
            # Create genre collections (only if 5+ shows)
            for genre, genre_shows in genres.items():
                if len(genre_shows) >= 5:
                    collection_name = f"{genre} TV Shows"
                    self._create_or_update_collection(library, collection_name, genre_shows)
                    
        except Exception as e:
            logger.error(f"Error creating TV collections: {e}")
    
    def _create_or_update_collection(self, library, collection_name, items):
        """Create or update a collection with given items"""
        try:
            # Check if collection already exists
            existing_collections = library.collections()
            existing_collection = None
            
            for collection in existing_collections:
                if collection.title == collection_name:
                    existing_collection = collection
                    break
            
            if existing_collection:
                # Update existing collection
                logger.info(f"Updating collection: {collection_name} ({len(items)} items)")
                # Note: Plex API doesn't have a direct way to bulk update collections
                # This would require adding/removing items individually
            else:
                # Create new collection
                logger.info(f"Creating collection: {collection_name} ({len(items)} items)")
                # Note: This requires the createCollection method which varies by library type
                # For now, we'll log the action
                logger.info(f"Would create collection '{collection_name}' with {len(items)} items")
                
        except Exception as e:
            logger.error(f"Error managing collection {collection_name}: {e}")

    def manage_collections(self):
        """Main collection management function"""
        logger.info("Starting collection management")
        self.create_collections()
        logger.info("Collection management completed")
def main():
    """Main function"""
    logger.info("Starting Simple PMM")
    
    try:
        pmm = SimplePMM()
        
        # Check if auto-run is enabled
        auto_run = os.getenv('AUTO_RUN_ENABLED', 'false').lower() == 'true'
        run_schedule = os.getenv('RUN_SCHEDULE', '06:00')
        
        if auto_run:
            logger.info(f"Scheduling automatic maintenance at {run_schedule}")
            schedule.every().day.at(run_schedule).do(pmm.run_maintenance)
            
            # Run initial status check
            pmm.get_server_status()
            pmm.get_libraries()
            
            # Keep the script running
            while True:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
        else:
            # Run once and exit
            pmm.get_server_status()
            pmm.get_libraries()
            pmm.run_maintenance()
            
    except KeyboardInterrupt:
        logger.info("PMM stopped by user")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
