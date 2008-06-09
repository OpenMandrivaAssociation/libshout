%define name	libshout
%define version	2.2.2
%define release	%mkrel 2

%define major		3
%define libname		%mklibname shout %{major}
%define develname	%mklibname shout -d

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A library for communicating with and sending data to an icecast server
Group:		System/Libraries
URL:		http://www.icecast.org/projects/libshout/
Source:		http://downloads.us.xiph.org/releases/libshout/%{name}-%{version}.tar.bz2
License:	LGPL+
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libtheora-devel
BuildRequires:	speex-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Libshout is a library for communicating with and sending data to an
icecast server.  It handles the socket connection, the timing of the
data, and prevents bad data from getting to the icecast server.

With just a few lines of code, a programmer can easily turn any
application into a streaming source for an icecast server.  Libshout also
allows developers who want a specific feature set (database access,
request taking) to concentrate on that feature set, instead of worrying
about how server communication works.

Please refer to the API reference and example code to start learning how
to use libshout in your own code.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/Other
Requires:	speex-devel
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname shout 3 -d}

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# remove installed doc
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/shout.pc
%{_datadir}/aclocal/shout.m4
