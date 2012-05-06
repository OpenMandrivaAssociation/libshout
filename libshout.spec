%define major 3
%define libname %mklibname shout %{major}
%define develname %mklibname shout -d

Summary:	A library for communicating with and sending data to an icecast server
Name:		libshout
Version:	2.3.0
Release:	2
Group:		System/Libraries
License:	LGPL+
URL:		http://www.icecast.org/
Source0:	http://downloads.us.xiph.org/releases/libshout/%{name}-%{version}.tar.gz
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libtheora-devel
BuildRequires:	speex-devel

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

%package -n	%{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n	%{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/Other
Requires:	speex-devel
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname shout 3 -d}

%description -n	%{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep

%setup -q

%build
autoreconf -fis
%configure2_5x
%make

%install
%makeinstall_std

# remove installed doc
rm -rf %{buildroot}%{_datadir}/doc/%{name}
rm -rf %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_libdir}/*.a

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{develname}
%doc README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/shout.pc
%{_datadir}/aclocal/shout.m4
