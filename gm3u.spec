# ===========================================================================
#                    Spec File for Package gm3u
# ===========================================================================

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Preamble
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Name:         gm3u
Summary:      Gnome enabled MP3 play-list editor
Version:      0.2
Release:      0
Copyright:    Free distributable
Group:        bb/mp3
Provides:     gm3u
Autoreqprov:  yes
Source:       gm3u-0.2.tar.gz
Vendor:       Bodo Bauer
Distribution: Bodo's Tools
Packager:     Bodo Bauer <bb@bb-zone.com>

%description
Gm3u is an MP3 play-list editor made with GTK+ toolkit 
and the Gome libraries. It allow you to create and edit
play-lists. The play-lists are stored as text files and can
be used with most MP3 players.

FEATURES
MP3 files can be selected in a file browser and then added
either to an existing play-list, or a new play-list will be 
created from scratch. Songs can be removed, moved up, moved down, 
moved to the end or to the beginning of the play-list.
If available, the ID3 tag of the MP3 file will be displayed when
the file is selected. Single songs can be played with an 
external MP3 player.


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Prep-Section
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
%prep
%setup -n gm3u-0.2
./configure --prefix=/usr/local

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Build-Section
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
%build
make

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Install-Section
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
%install

make install

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Clean up
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
%clean

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# File-List
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
%files
/usr/local/bin/gm3u
%doc AUTHORS COPYING ChangeLog INSTALL README NEWS
