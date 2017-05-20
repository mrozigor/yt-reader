#!/usr/bin/env python

import sys
import sqlite3
import os.path

if len(sys.argv) == 1:
    print("\nUsage: " + sys.argv[0] + " <command> (<parameter>)\n")
    print("Commands:")
    print("-addkey <key> -> save YT API key,")
    print("-showkey -> show current YT API key,")
    print("-search <user_id> -> will display all playlist for given user,")
    print("-showlist -> shows all saved playlists,")
    print("-playlist <playlist_id> -> show all videos from given playlist,")
    print("-mark <video_id> -> (un)mark given video.\n")
    sys.exit(1)

if not os.path.isfile("database"):
    connection = sqlite3.connect("database")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE config (name text, value text)")
    cursor.execute("CREATE TABLE playlists (name text, user text, playlist_id integer)")
    cursor.execute("CREATE TABLE videos (title text, url text, published_at text, status integer, playlist_id integer)")
    connection.commit()
    connection.close()
    
if sys.argv[1] == "-addkey":
    if len(sys.argv) == 3:
        print("Key added")
elif sys.argv[1] == "-showkey":
    print("showkey")
elif sys.argv[1] == "-search":
    print("search")
elif sys.argv[1] == "-showlist":
    print("showlist")
elif sys.argv[1] == "-playlist":
    print("playlist")
elif sys.argv[1] == "-mark":
    print("mark")
else:
    print("Unrecognized command. Run application without arguments to see help.")
