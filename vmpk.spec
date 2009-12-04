Summary:	Virtual MIDI piano keyboard
Summary(pl.UTF-8):	Wirutalna MIDI klawiatura pianina
Name:		vmpk
Version:	0.2.6
Release:	1
License:	GPL v3
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/vmpk/%{name}-%{version}.tar.bz2
# Source0-md5:	5f25fbbe139f7e1f3f3e9df321d24f0c
Patch0:		%{name}-locale.patch
Patch1:		%{name}-desktop.patch
URL:		http://vmpk.sourceforge.net/
BuildRequires:	QtGui-devel >= 4.4.0
BuildRequires:	QtXml-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	cmake
BuildRequires:	pkgconfig
BuildRequires:	qt4-build
BuildRequires:	qt4-linguist
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.471
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Virtual MIDI Piano Keyboard is a MIDI events generator and receiver.
It doesn't produce any sound by itself, but can be used to drive a
MIDI synthesizer (either hardware or software, internal or external).
You can use the computer's keyboard to play MIDI notes, and also the
mouse.

%description -l pl.UTF-8
Wirtualna MIDI klawiatura pianina generuje i odbiera zdarzenia MIDI.
Sam program nie produkuje żadnych dźwięków, ale może być używany do
kierowania syntezatorem MIDI (sprzętowego lub programowego,
wewnętrznego bądź zewnętrznego). Możesz korzystać z klawiatury
komputera lub myszy do grania dźwięków MIDI.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
install -d build

cd build
%cmake .. \
	-DCMAKE_INSTALL_PREFIX=%{_prefix}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/vmpk.desktop
%{_mandir}/man1/vmpk.1*
%{_datadir}/vmpk
%{_iconsdir}/hicolor/16x16/apps/vmpk.png
%{_iconsdir}/hicolor/32x32/apps/vmpk.png
%{_iconsdir}/hicolor/48x48/apps/vmpk.png
%{_iconsdir}/hicolor/64x64/apps/vmpk.png
%{_iconsdir}/hicolor/scalable/apps/vmpk.svg
