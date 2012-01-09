Name:		beret
Version:	1.2.0
Release:	1
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

%files
%{_bindir}/%{name}
