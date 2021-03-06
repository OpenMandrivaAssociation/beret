Name:		beret
Version:	1.2.0
Release:	5
Summary:	2D puzzle platformer
Group:		Games/Arcade
Url:		http://kiwisauce.com
Source0:	%{name}.tar.bz2
License:	GPLv2
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_ttf)
BuildRequires:	pkgconfig(SDL_mixer)
Patch0:		math_lib.patch

%description
Beret is a 2D puzzle platformer about a 
telekinetic scientist that is available for Windows, Mac OS X, and Linux.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
#cp /usr/include/SDL/* ./
%make

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}
#install data

mkdir -p %{buildroot}%{_datadir}/%{name}/images
install -m 0644 images/*.{png,bmp} %{buildroot}%{_datadir}/%{name}/images
#install music
mkdir -p %{buildroot}%{_datadir}/%{name}/music
install -m 0644 music/*.ogg %{buildroot}%{_datadir}/%{name}/music
#install sfx
mkdir -p %{buildroot}%{_datadir}/%{name}/sfx
install -m 0644 sfx/*.wav %{buildroot}%{_datadir}/%{name}/sfx
#install rooms
mkdir -p %{buildroot}%{_datadir}/%{name}/rooms
install -m 0644 rooms/* %{buildroot}%{_datadir}/%{name}/rooms
#font
install -m 0644 AveriaSans-Regular.ttf  %{buildroot}%{_datadir}/%{name}/

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/images/*
%{_datadir}/%{name}/music/*
%{_datadir}/%{name}/sfx/*
%{_datadir}/%{name}/rooms/*
%{_datadir}/%{name}/AveriaSans-Regular.ttf


%changelog
* Tue Jan 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.0-2
+ Revision: 759349
- AveriaSans-Regular font needed for game
- music sfx rooms added

* Mon Jan 09 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.0-1
+ Revision: 759211
- music and pictures added
- imported package beret

