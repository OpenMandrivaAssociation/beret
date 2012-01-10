Name:		beret
Version:	1.2.0
Release:	2
Summary:	Beret is a 2D puzzle platformer
Group:		Games/Arcade
Url:		http://kiwisauce.com
Source0:	%{name}.tar.bz2
License:	GPLv2
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_mixer-devel
Patch0:		math_lib.patch

%description
Beret is a 2D puzzle platformer about a 
telekinetic scientist that is available for Windows, Mac OS X, and Linux.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
cp /usr/include/SDL/* ./
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
