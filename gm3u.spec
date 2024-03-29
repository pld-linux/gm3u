Summary:	GNOME enabled MP3 play-list editor
Summary(pl.UTF-8):	Edytor playlist MP3 dla GNOME
Name:		gm3u
Version:	0.2
Release:	4
License:	GPL
Vendor:		Bodo Bauer
Group:		X11/Applications/Sound
Source0:	ftp://ftp.bb-zone.com/pub/gm3u/%{name}-%{version}.tar.gz
# Source0-md5:	b248b90599e0497459d1b1d07b5c4ec9
URL:		http://www.bb-zone.com/gm3u/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gm3u is an MP3 play-list editor made with GTK+ toolkit and the Gome
libraries. It allow you to create and edit play-lists. The play-lists
are stored as text files and can be used with most MP3 players.
FEATURES MP3 files can be selected in a file browser and then added
either to an existing play-list, or a new play-list will be created
from scratch. Songs can be removed, moved up, moved down, moved to the
end or to the beginning of the play-list. If available, the ID3 tag of
the MP3 file will be displayed when the file is selected. Single songs
can be played with an external MP3 player.

%description -l pl.UTF-8
Gm3u jest edytorem list plików MP3 do odtwarzania; został napisany z
wykorzystaniem GTK+ i bibliotek GNOME. Pozwala tworzyć i modyfikować
listy plików do odtworzenia; są one przechowywane w plikach tekstowych
obsługiwanych przez większość odtwarzaczy MP3. Funkcje: można
zaznaczyć pliki MP3 w przeglądarce plików i/lub dodać je do
istniejącej listy plików, albo utworzyć nową listę. Można usuwać i
przesuwać utwory w kolejce. Jeśli plik MP3 zawiera znacznik ID3,
będzie on wyświetlony podczas wyboru pliku. Pojedyncze pliki można
odgrywać za pomocą zewnętrznego odtwarzacza.

%prep
%setup -q

%build
#echo | gettextize --copy --force
%{__aclocal} -I macros
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

#%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS
%attr(755,root,root) %{_bindir}/gm3u
