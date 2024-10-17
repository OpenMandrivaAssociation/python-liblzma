%define	oname	pyliblzma
%define	module	liblzma

Summary:	Python bindings for liblzma
Name:		python-%{module}
Version:	0.5.3
Release:	%mkrel 3
License:	LGPLv3+
Group:		Development/Python
Url:		https://lzmautils.sourceforge.net/
Source0:	%{oname}-%{version}.tar.xz
%py_requires -d
BuildRequires:	liblzma-devel >= 4.999.8beta python-setuptools
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
PylibLZMA provides a python interface for the liblzma library
to read and write data that has been compressed or can be decompressed
by Lasse Collin's lzma utils.

%prep
%setup -qn %{oname}-%{version}

%build
python setup.py build

%check
python setup.py test

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README THANKS ChangeLog
%{python_sitearch}/lzma.so
%{python_sitearch}/%{module}.py*
%{python_sitearch}/%{oname}*.egg-info


%changelog
* Sat Nov 27 2010 Funda Wang <fwang@mandriva.org> 0.5.3-3mdv2011.0
+ Revision: 601640
- rebuild for new liblzma

* Sun Oct 31 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.5.3-2mdv2011.0
+ Revision: 590770
- rebuild for new python 2.7

* Tue Apr 13 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.5.3-1mdv2010.1
+ Revision: 534615
- new release: 0.5.3

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.5.2-2mdv2010.0
+ Revision: 442262
- rebuild

* Thu Feb 26 2009 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.5.2-1mdv2009.1
+ Revision: 345302
- new release: 0.5.2

* Sun Jan 25 2009 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.5.0-1mdv2009.1
+ Revision: 333379
- new release (adds xz support \o/)

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 0.4.1-2mdv2009.1
+ Revision: 319567
- rebuild with python 2.6

* Fri Oct 24 2008 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.4.1-1mdv2009.1
+ Revision: 296938
- new release: 0.4.1 (fixes compatibility with new liblzma api)
- new release

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.3.1-2mdv2009.0
+ Revision: 269032
- rebuild early 2009.0 package (before pixel changes)

* Fri May 23 2008 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.3.1-1mdv2009.0
+ Revision: 210362
- new release: 0.3.1

* Tue May 20 2008 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.3-1mdv2009.0
+ Revision: 209447
- import python-liblzma


* Mon May 19 2008 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.3-1
- initial release
