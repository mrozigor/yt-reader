#!/usr/bin/env python

import sys

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

if sys.argv[1] == "-addkey":
    print("addkey")
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
