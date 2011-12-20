Summary:	Max Fighter vertical shoot'em up
Summary(pl.UTF-8):	Strzelanka kosmiczna Max Fighter
Name:		maxfighter
Version:	1.0.1
Release:	2
License:	GPL, Creative Commons NCSA 2.5
Group:		X11/Applications/Games
Source0:	http://source.musgit.com/files/%{name}_%{version}.tar.bz2
# Source0-md5:	086b008982666a839d9a293016ec4591
Patch0:		%{name}-scons.patch
URL:		http://maxfighter.musgit.com/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL_image-devel
BuildRequires:	expat-devel
BuildRequires:	libpng-devel
BuildRequires:	libvorbis-devel
BuildRequires:	mysdl
BuildRequires:	scons
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Max Fighter vertical shoot'em up.

%description -l pl.UTF-8
Strzelanka kosmiczna Max Fighter.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1

%build
sed -i "/RESOURCEDIR/s|resources/|/usr/share/games/%{name}/|" SConstruct
%{__scons} \
	%{!?debug:dist=1} \
	CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/%{name},/var/games/%{name}}

install build/linux/%{name} $RPM_BUILD_ROOT%{_bindir}
cp -r resources/* $RPM_BUILD_ROOT%{_datadir}/games/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%attr(2755,root,games) %{_bindir}/%{name}
%{_datadir}/games/%{name}
%attr(770,root,games) %dir /var/games/%{name}
