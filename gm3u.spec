Summary:	Gnome enabled MP3 play-list editor
Name:		gm3u
Version:	0.2
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Vendor:		Bodo Bauer
Source0:	ftp://ftp.bb-zone.com/pub/gm3u/%{name}-%{version}.tar.gz
URL:		http://www.bb-zone.com/gm3u/
#BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6

%description
Gm3u is an MP3 play-list editor made with GTK+ toolkit and the Gome
libraries. It allow you to create and edit play-lists. The play-lists are
stored as text files and can be used with most MP3 players. FEATURES MP3
files can be selected in a file browser and then added either to an
existing play-list, or a new play-list will be created from scratch. Songs
can be removed, moved up, moved down, moved to the end or to the beginning
of the play-list. If available, the ID3 tag of the MP3 file will be
displayed when the file is selected. Single songs can be played with an
external MP3 player.

%prep
%setup -q
%configure

%build
#echo | gettextize --copy --force
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

gzip -9nf AUTHORS ChangeLog README NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gm3u
