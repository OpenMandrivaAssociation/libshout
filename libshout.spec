%define major 3
%define libname %mklibname shout %{major}
%define develname %mklibname shout -d

Summary:	A library for communicating with and sending data to an icecast server
Name:		libshout
Version:	2.3.1
Release:	2
Group:		System/Libraries
License:	LGPL+
URL:		http://www.icecast.org/
Source0:	http://downloads.us.xiph.org/releases/libshout/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(speex)

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
Requires:	pkgconfig(speex)
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname shout 3 -d} < 2.3.1

%description -n	%{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q

%build
autoreconf -fis
%configure2_5x --disable-static
%make

%install
%makeinstall_std

# remove installed doc
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{develname}
%doc README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/shout.pc
%{_datadir}/aclocal/shout.m4


%changelog
* Mon Jun 25 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.3.1-1
+ Revision: 806785
- version update 2.3.1

* Mon May 07 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.3.0-2
+ Revision: 797229
- rebuild

* Mon Feb 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.3.0-1
+ Revision: 778133
- version update 2.3.0

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 2.2.2-8
+ Revision: 661526
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.2-7mdv2011.0
+ Revision: 602606
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.2-6mdv2010.1
+ Revision: 520906
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.2.2-5mdv2010.0
+ Revision: 425742
- rebuild

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 2.2.2-4mdv2009.0
+ Revision: 229863
- fix speex linkage (P0)
- spec file massage

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 2.2.2-2mdv2008.1
+ Revision: 150825
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Aug 03 2007 Adam Williamson <awilliamson@mandriva.org> 2.2.2-1mdv2008.0
+ Revision: 58465
- rebuild for 2008
- Fedora license policy
- new devel policy
- spec clean
- Import libshout

