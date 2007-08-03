%define name        libshout
%define version     2.2.2
%define release     %mkrel  1
%define lib_major   3
%define lib_name    %mklibname shout %{lib_major}

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    A library for communicating with and sending data to an icecast server
Group:      System/Libraries
URL:        http://www.icecast.org/projects/libshout/
Source:     http://downloads.us.xiph.org/releases/libshout/%{name}-%{version}.tar.bz2
License:    LGPL
BuildRequires:  libogg-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libtheora-devel
BuildRequires:  speex-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Libshout is a library for communicating with and sending data to an
icecast server.  It handles the socket connection, the timing of the
data, and prevents bad data from getting to the icecast server.

With just a few lines of code, a programmer can easily turn any
application into a streaming source for an icecast server.  Libshout also
allows developers who want a specific feature set (database access,
request taking) to concentrate on that feature set, instead of worrying
about how server communication works.

Please refer to the api reference and example code to start learning how
to use libshout in your own code.

Libshout is licensed under the LGPL.  Please see the COPYING file for 
details.

If you have any questions or comments, please visit us at 
http://www.icecast.org or email us at team@icecast.org.

%package -n %{lib_name}
Summary:    Main library for %{name}
Group:      System/Libraries

%description -n %{lib_name}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{lib_name}-devel
Summary:    Headers for developing programs that will use %{name}
Group:      Development/Other
Requires:   speex-devel
Requires:   %{lib_name} = %{version}
Provides:   %{name}-devel = %{version}-%{release}

%description -n %{lib_name}-devel
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

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%doc README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/shout.pc
%{_datadir}/aclocal/shout.m4
