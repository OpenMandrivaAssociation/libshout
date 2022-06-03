%define major	3
%define libname	%mklibname shout %{major}
%define devname	%mklibname shout -d

Summary:	A library for communicating with and sending data to an icecast server
Name:		libshout
Version:	2.4.6
Release:	1
Group:		System/Libraries
License:	LGPLv2+
Url:		http://www.icecast.org/
Source0:	http://downloads.us.xiph.org/releases/libshout/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(speex)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(vorbis)

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

%package -n	%{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q
%autopatch -p1
autoreconf -fis
%configure

%build
%make_build

%install
%make_install

# remove installed doc
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%files
%{_bindir}/shout
%{_mandir}/man1/shout.1*

%files -n %{libname}
%{_libdir}/libshout.so.%{major}*

%files -n %{devname}
%doc README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/shout.pc
%{_datadir}/aclocal/shout.m4
%{_libdir}/ckport/db/libshout.ckport
