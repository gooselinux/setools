%define setools_maj_ver 3.3
%define setools_min_ver 7
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name: setools
Version: %{setools_maj_ver}.%{setools_min_ver}
Release: 4%{?dist}
License: GPLv2
URL: http://oss.tresys.com/projects/setools
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Source: http://oss.tresys.com/projects/setools/chrome/site/dists/setools-%{version}/setools-%{version}.tar.bz2
Source1: setools.pam
Source2: apol.desktop
Source3: seaudit.desktop
Source4: sediffx.desktop
Patch1: setools-python.patch
Patch2: setools-rhat.patch
Summary: Policy analysis tools for SELinux
Group: System Environment/Base
Requires: setools-libs = %{version}-%{release} setools-libs-tcl = %{version}-%{release} setools-gui = %{version}-%{release} setools-console = %{version}-%{release}

# external requirements
%define autoconf_ver 2.59
%define bwidget_ver 1.8
%define java_ver 1.2
%define gtk_ver 2.8
%define python_ver 2.3
%define sepol_ver 1.12.27
%define selinux_ver 1.30
%define sqlite_ver 3.2.0
%define swig_ver 1.3.28
%define tcltk_ver 8.4.9

%description
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This meta-package depends upon the main packages necessary to run
SETools.

%package libs
License: LGPLv2
Summary: Policy analysis support libraries for SELinux
Group: System Environment/Libraries
Requires: libselinux >= %{selinux_ver} libsepol >= %{sepol_ver} sqlite >= %{sqlite_ver}
BuildRequires: flex  bison  pkgconfig
BuildRequires: glibc-devel libstdc++-devel gcc gcc-c++
BuildRequires: libselinux-devel >= %{selinux_ver} libsepol-devel >= %{sepol_ver}
BuildRequires: libsepol-static >= %{sepol_ver}
BuildRequires: sqlite-devel >= %{sqlite_ver} libxml2-devel
BuildRequires: tcl-devel >= %{tcltk_ver}
BuildRequires: autoconf >= %{autoconf_ver} automake

%description libs
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes the following run-time libraries:

  libapol       policy analysis library
  libpoldiff    semantic policy difference library
  libqpol       library that abstracts policy internals
  libseaudit    parse and filter SELinux audit messages in log files
  libsefs       SELinux file contexts library

%package libs-python
License: LGPLv2
Summary: Python bindings for SELinux policy analysis
Group: Development/Languages
Requires: setools-libs = %{version}-%{release} python2 >= %{python_ver} bzip2-libs
BuildRequires: python2-devel >= %{python_ver} swig >= %{swig_ver} bzip2-devel

%description libs-python
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes Python bindings for the following libraries:

  libapol       policy analysis library
  libpoldiff    semantic policy difference library
  libqpol       library that abstracts policy internals
  libseaudit    parse and filter SELinux audit messages in log files
  libsefs       SELinux file contexts library

%package libs-java
License: LGPLv2
Summary: Java bindings for SELinux policy analysis
Group: Development/Languages
Requires: setools-libs = %{version}-%{release} java >= %{java_ver}
BuildRequires: java-devel >= %{java_ver} swig >= %{swig_ver}

%description libs-java
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes Java bindings for the following libraries:

  libapol       policy analysis library
  libpoldiff    semantic policy difference library
  libqpol       library that abstracts policy internals
  libseaudit    parse and filter SELinux audit messages in log files
  libsefs       SELinux file contexts library

%package libs-tcl
License: LGPLv2
Summary: Tcl bindings for SELinux policy analysis
Group: Development/Languages
Requires: setools-libs = %{version}-%{release} tcl >= %{tcltk_ver}
BuildRequires: tcl-devel >= %{tcltk_ver} swig >= %{swig_ver}

%description libs-tcl
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes Tcl bindings for the following libraries:

  libapol       policy analysis library
  libpoldiff    semantic policy difference library
  libqpol       library that abstracts policy internals
  libseaudit    parse and filter SELinux audit messages in log files
  libsefs       SELinux file contexts library

%package devel
License: LGPLv2
Summary: Policy analysis development files for SELinux
Group: Development/Libraries
Requires: libselinux-devel >= %{selinux_ver} libsepol-devel >= %{sepol_ver} setools-libs = %{version}-%{release}
BuildRequires: sqlite-devel >= %{sqlite_ver} libxml2-devel

%description devel
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes header files and archives for the following
libraries:

  libapol       policy analysis library
  libpoldiff    semantic policy difference library
  libqpol       library that abstracts policy internals
  libseaudit    parse and filter SELinux audit messages in log files
  libsefs       SELinux file contexts library

%package console
Summary: Policy analysis command-line tools for SELinux
Group: System Environment/Base
License: GPLv2
Requires: setools-libs = %{version}-%{release}
Requires: libselinux >= %{selinux_ver}

%description console
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes the following console tools:

  seaudit-report  audit log analysis tool
  sechecker       SELinux policy checking tool
  secmds          command line tools: seinfo, sesearch, findcon,
                  replcon, and indexcon
  sediff          semantic policy difference tool

%package gui
Summary: Policy analysis graphical tools for SELinux
Group: System Environment/Base
Requires: tcl >= %{tcltk_ver} tk >= %{tcltk_ver} bwidget >= %{bwidget_ver}
Requires: setools-libs = %{version}-%{release} setools-libs-tcl = %{version}-%{release}
Requires: glib2 gtk2 >= %{gtk_ver} usermode
BuildRequires: gtk2-devel >= %{gtk_ver} libglade2-devel libxml2-devel tk-devel >= %{tcltk_ver}
BuildRequires: desktop-file-utils

%description gui
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes the following graphical tools:

  apol          policy analysis tool
  seaudit       audit log analysis tool
  sediffx       semantic policy difference tool

%define setoolsdir %{_datadir}/setools-%{setools_maj_ver}
%define pkg_py_lib %{python_sitelib}/setools
%define pkg_py_arch %{python_sitearch}/setools
%define javajardir %{_datadir}/java
%define tcllibdir %{_libdir}/setools

%prep
%setup -q
%patch1 -p 1 -b .python
%patch2 -p 1 -b .rhat

%build
%configure --libdir=%{_libdir} --disable-bwidget-check --disable-selinux-check \
    --enable-swig-python --enable-swig-java --enable-swig-tcl --with-java-prefix=/usr/lib/jvm/java
# work around issue with gcc 4.3 + gnu99 + swig-generated code:
sed -i -e 's:$(CC):gcc -std=gnu89:' libseaudit/swig/python/Makefile
%ifarch sparc sparcv9 sparc64 s390 s390x                                                                                                
    for file in `find . -name Makefile`; do                                                                                             
        sed -i -e 's:-fpic:-fPIC:' $file;                                                                                               
    done                                                                                                                                
%endif           
make %{?_smp_mflags}

%install
rm -rf ${RPM_BUILD_ROOT}
make DESTDIR=${RPM_BUILD_ROOT} INSTALL="install -p" install
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/applications
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/pixmaps
install -d -m 755 ${RPM_BUILD_ROOT}%{_sysconfdir}/pam.d
install -p -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/pam.d/seaudit
install -d -m 755 ${RPM_BUILD_ROOT}%{_sysconfdir}/security/console.apps
install -p -m 644 packages/rpm/seaudit.console ${RPM_BUILD_ROOT}%{_sysconfdir}/security/console.apps/seaudit
install -d -m 755 ${RPM_BUILD_ROOT}%{_datadir}/applications
install -p -m 644 apol/apol.png ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/apol.png
install -p -m 644 seaudit/seaudit.png ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/seaudit.png
install -p -m 644 sediff/sediffx.png ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/sediffx.png
desktop-file-install --dir ${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE2} %{SOURCE3} %{SOURCE4}
ln -sf consolehelper ${RPM_BUILD_ROOT}/%{_bindir}/seaudit
# replace absolute symlinks with relative symlinks
ln -sf ../setools-%{setools_maj_ver}/qpol.jar ${RPM_BUILD_ROOT}/%{javajardir}/qpol.jar
ln -sf ../setools-%{setools_maj_ver}/apol.jar ${RPM_BUILD_ROOT}/%{javajardir}/apol.jar
ln -sf ../setools-%{setools_maj_ver}/poldiff.jar ${RPM_BUILD_ROOT}/%{javajardir}/poldiff.jar
ln -sf ../setools-%{setools_maj_ver}/seaudit.jar ${RPM_BUILD_ROOT}/%{javajardir}/seaudit.jar
ln -sf ../setools-%{setools_maj_ver}/sefs.jar ${RPM_BUILD_ROOT}/%{javajardir}/sefs.jar
# remove static libs
rm -f ${RPM_BUILD_ROOT}/%{_libdir}/*.a
# ensure permissions are correct
chmod 0755 ${RPM_BUILD_ROOT}/%{_libdir}/*.so.*
chmod 0755 ${RPM_BUILD_ROOT}/%{_libdir}/%{name}/*/*.so.*
chmod 0755 ${RPM_BUILD_ROOT}/%{pkg_py_arch}/*.so.*
chmod 0755 ${RPM_BUILD_ROOT}/%{setoolsdir}/seaudit-report-service
chmod 0644 ${RPM_BUILD_ROOT}/%{tcllibdir}/*/pkgIndex.tcl

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root,-)

%files libs
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING COPYING.GPL COPYING.LGPL KNOWN-BUGS NEWS README
%{_libdir}/libqpol.so.*
%{_libdir}/libapol.so.*
%{_libdir}/libpoldiff.so.*
%{_libdir}/libsefs.so.*
%{_libdir}/libseaudit.so.*
%dir %{setoolsdir}

%files libs-python
%defattr(-,root,root,-)
%{pkg_py_lib}/
%ifarch x86_64 ppc64 sparc64 s390x
%{pkg_py_arch}/
%endif
%{python_sitearch}/setools*.egg-info

%files libs-java
%defattr(-,root,root,-)
%{_libdir}/libjqpol.so.*
%{_libdir}/libjapol.so.*
%{_libdir}/libjpoldiff.so.*
%{_libdir}/libjseaudit.so.*
%{_libdir}/libjsefs.so.*
%{setoolsdir}/*.jar
%{javajardir}/*.jar

%files libs-tcl
%defattr(-,root,root,-)
%dir %{tcllibdir}
%{tcllibdir}/qpol/
%{tcllibdir}/apol/
%{tcllibdir}/poldiff/
%{tcllibdir}/seaudit/
%{tcllibdir}/sefs/

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/qpol/
%{_includedir}/apol/
%{_includedir}/poldiff/
%{_includedir}/seaudit/
%{_includedir}/sefs/

%files console
%defattr(-,root,root,-)
%{_bindir}/seinfo
%{_bindir}/sesearch
%{_bindir}/indexcon
%{_bindir}/findcon
%{_bindir}/replcon
%{_bindir}/sechecker
%{_bindir}/sediff
%{_bindir}/seaudit-report
%{setoolsdir}/sechecker-profiles/
%{setoolsdir}/sechecker_help.txt
%{setoolsdir}/seaudit-report-service
%{setoolsdir}/seaudit-report.conf
%{setoolsdir}/seaudit-report.css
%{_mandir}/man1/findcon.1.gz
%{_mandir}/man1/indexcon.1.gz
%{_mandir}/man1/replcon.1.gz
%{_mandir}/man1/sechecker.1.gz
%{_mandir}/man1/sediff.1.gz
%{_mandir}/man1/seinfo.1.gz
%{_mandir}/man1/sesearch.1.gz
%{_mandir}/man8/seaudit-report.8.gz

%files gui
%defattr(-,root,root,-)
%{_bindir}/seaudit
%{_bindir}/sediffx
%{_bindir}/apol
%{tcllibdir}/apol_tcl/
%{setoolsdir}/sediff_help.txt
%{setoolsdir}/apol_help.txt
%{setoolsdir}/domaintrans_help.txt
%{setoolsdir}/file_relabel_help.txt
%{setoolsdir}/infoflow_help.txt
%{setoolsdir}/types_relation_help.txt
%{setoolsdir}/apol_perm_mapping_*
%{setoolsdir}/seaudit_help.txt
%{setoolsdir}/*.glade
%{setoolsdir}/*.png
%{setoolsdir}/apol.gif
%{setoolsdir}/dot_seaudit
%{_mandir}/man1/apol.1.gz
%{_mandir}/man1/sediffx.1.gz
%{_mandir}/man8/seaudit.8.gz
%{_sbindir}/seaudit
%config(noreplace) %{_sysconfdir}/pam.d/seaudit
%config(noreplace) %{_sysconfdir}/security/console.apps/seaudit
%{_datadir}/applications/*
%attr(0644,root,root) %{_datadir}/pixmaps/*.png

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%post libs-java -p /sbin/ldconfig

%postun libs-java -p /sbin/ldconfig

%post libs-tcl -p /sbin/ldconfig

%postun libs-tcl -p /sbin/ldconfig

%changelog
* Tue Aug 16 2010 Dan Walsh <dwalsh@redhat.com> 3.3.7-4
- Make sesearch -all work
Resolves: #583915

* Tue Jun 15 2010 Dan Walsh <dwalsh@redhat.com> 3.3.7-3
- Make sesearch -all work
Resolves: #583915

* Wed May 12 2010 Chris PeBenito <cpebenito@tresys.com> 3.3.7-2
- Add missing bzip2 dependencies.

* Wed May 12 2010 Chris PeBenito <cpebenito@tresys.com> 3.3.7-1
- New upstream release.

* Tue Aug 11 2009 Dan Walsh <dwalsh@redhat.com> 3.3.6-4
- Add python bindings for sesearch and seinfo

* Tue Jul 28 2009 Dan Walsh <dwalsh@redhat.com> 3.3.6-3
- Fix qpol install of include files

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Chris PeBenito <cpebenito@tresys.com> 3.3.6-1
- New upstream release.

* Sun Apr  5 2009 Dan Horák <dan[at]danny.cz> - 3.3.5-8
- don't expect that java-devel resolves as gcj

* Sun Apr  5 2009 Dan Horák <dan[at]danny.cz> - 3.3.5-7
- add support for s390x

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 04 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.3.5-5
- Rebuild for Python 2.6

* Mon Dec  1 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 3.3.5-4
- Include %%tcllibdir directory in -libs-tcl package.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.3.5-3
- Rebuild for Python 2.6

* Wed Sep 17 2008 Dennis Gilmore <dennis@ausil.us> 3.3.5-2
- fix building in sparc and s390 arches

* Tue Aug 26 2008 Chris PeBenito <cpebenito@tresys.com> 3.3.5-1
- Update to upstream version 3.3.5.

* Wed Feb 27 2008 Chris PeBenito <cpebenito@tresys.com> 3.3.4-1
- Fixes gcc 4.3, glibc 2.7, tcl 8.5, and libsepol 2.0.20 issues.
- Fix policy loading when policy on disk is higher version than the kernel.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.3.2-3
- Autorebuild for GCC 4.3

* Tue Jan 29 2008 Chris Pebenito <cpebenito@tresys.com> 3.3.2-2.fc9
- Bump to pick up new libsepol and policy 22.

* Wed Nov 28 2007 Chris Pebenito <cpebenito@tresys.com> 3.3.2-1.fc9
- Update for 3.3.2.

* Thu Oct 18 2007 Chris PeBenito <cpebenito@tresys.com> 3.3.1-7.fc8
- Rebuild to fix ppc64 issue.

* Wed Oct 17 2007 Chris PeBenito <cpebenito@tresys.com> 3.3.1-6.fc8
- Update for 3.3.1.

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 3.2-4
- Rebuild for selinux ppc32 issue.

* Fri Jul 20 2007 Dan Walsh <dwalsh@redhat.com> 3.2-3
- Move to Tresys spec file

* Wed Jun 13 2007 Dan Walsh <dwalsh@redhat.com> 3.2-2
- Bump for rebuild

* Mon Apr 30 2007 Dan Walsh <dwalsh@redhat.com> 3.2-1
- Start shipping the rest of the setools command line apps

* Wed Apr 25 2007 Jason Tang <jtang@tresys.com> 3.2-0
- update to SETools 3.2 release

* Mon Feb 02 2007 Jason Tang <jtang@tresys.com> 3.1-1
- update to SETools 3.1 release

* Mon Oct 30 2006 Dan Walsh <dwalsh@redhat.com> 3.0-2.fc6
- bump for fc6
 
* Thu Oct 26 2006 Dan Walsh <dwalsh@redhat.com> 3.0-2
- Build on rawhide

* Sun Oct 15 2006 Dan Walsh <dwalsh@redhat.com> 3.0-1
- Update to upstream

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Tue May 23 2006 Dan Walsh <dwalsh@redhat.com> 2.4-2
- Remove sqlite include directory

* Wed May 3 2006 Dan Walsh <dwalsh@redhat.com> 2.4-1
- Update from upstream

* Mon Apr 10 2006 Dan Walsh <dwalsh@redhat.com> 2.3-3
- Fix help
- Add icons

* Tue Mar 21 2006 Dan Walsh <dwalsh@redhat.com> 2.3-2
- Remove console apps for sediff, sediffx and apol

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.3-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.3-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Dan Walsh <dwalsh@redhat.com> 2.3-1
- Update from upstream
  * apol:
        added new MLS components tab for sensitivities, 
        levels, and categories.
        Changed users tab to support ranges and default 
        levels.
        added range transition tab for searching range
        Transition rules.
        added new tab for network context components.
        added new tab for file system context components.
  * libapol:
        added binpol support for MLS, network contexts, 
        and file system contexts.
  * seinfo:
        added command line options for MLS components.
        added command line options for network contexts
        and file system contexts.
  * sesearch:
        added command line option for searching for rules
        by conditional boolean name.
  * seaudit:
        added new column in the log view for the 'comm' 
        field found in auditd log files.
        added filters for the 'comm' field and 'message'
        field.
  * manpages:
        added manpages for all tools.        



* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Wed Dec 14 2005 Dan Walsh <dwalsh@redhat.com> 2.2-4
- Fix dessktop files
- Apply fixes from bkyoung

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Nov 3 2005 Dan Walsh <dwalsh@redhat.com> 2.2-3
- Move more gui files out of base into gui 

* Thu Nov 3 2005 Dan Walsh <dwalsh@redhat.com> 2.2-2
- Move sediff from gui to main package

* Thu Nov 3 2005 Dan Walsh <dwalsh@redhat.com> 2.2-1
- Upgrade to upstream version

* Thu Oct 13 2005 Dan Walsh <dwalsh@redhat.com> 2.1.3-1
- Upgrade to upstream version

* Mon Oct 10 2005 Tomas Mraz <tmraz@redhat.com> 2.1.2-3
- use include instead of pam_stack in pam config

* Thu Sep 1 2005 Dan Walsh <dwalsh@redhat.com> 2.1.2-2
- Fix spec file
 
* Thu Sep 1 2005 Dan Walsh <dwalsh@redhat.com> 2.1.2-1
- Upgrade to upstream version
 
* Thu Aug 18 2005 Florian La Roche <laroche@redhat.com>
- do not package debug files into the -devel package

* Wed Aug 17 2005 Jeremy Katz <katzj@redhat.com> - 2.1.1-3
- rebuild against new cairo

* Wed May 25 2005 Dan Walsh <dwalsh@redhat.com> 2.1.1-0
- Upgrade to upstream version

* Mon May 23 2005 Bill Nottingham <notting@redhat.com> 2.1.0-5
- put libraries in the right place (also puts debuginfo in the right
  package)
- add %%defattr for -devel too

* Thu May 12 2005 Dan Walsh <dwalsh@redhat.com> 2.1.0-4
- Move sepcut to gui apps.

* Fri May 6 2005 Dan Walsh <dwalsh@redhat.com> 2.1.0-3
- Fix Missing return code.

* Wed Apr 20 2005 Dan Walsh <dwalsh@redhat.com> 2.1.0-2
- Fix requires line

* Tue Apr 19 2005 Dan Walsh <dwalsh@redhat.com> 2.1.0-1
- Update to latest from tresys

* Tue Apr 5 2005 Dan Walsh <dwalsh@redhat.com> 2.0.0-2
- Fix buildrequires lines in spec file

* Tue Mar 2 2005 Dan Walsh <dwalsh@redhat.com> 2.0.0-1
- Update to latest from tresys

* Mon Nov 29 2004 Dan Walsh <dwalsh@redhat.com> 1.5.1-6
- add FALLBACK=true to /etc/security/console.apps/apol

* Wed Nov 10 2004 Dan Walsh <dwalsh@redhat.com> 1.5.1-3
- Add badtcl patch from Tresys.

* Mon Nov 8 2004 Dan Walsh <dwalsh@redhat.com> 1.5.1-2
- Apply malloc problem patch provided by  Sami Farin 

* Mon Nov 1 2004 Dan Walsh <dwalsh@redhat.com> 1.5.1-1
- Update to latest from Upstream

* Wed Oct 6 2004 Dan Walsh <dwalsh@redhat.com> 1.4.1-5
- Update tresys patch

* Mon Oct 4 2004 Dan Walsh <dwalsh@redhat.com> 1.4.1-4
- Fix directory ownership

* Thu Jul 8 2004 Dan Walsh <dwalsh@redhat.com> 1.4.1-1
- Latest from Tresys

* Wed Jun 23 2004 Dan Walsh <dwalsh@redhat.com> 1.4-5
- Add build requires libselinux

* Tue Jun 22 2004 Dan Walsh <dwalsh@redhat.com> 1.4-4
- Add support for policy.18

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jun 10 2004 Dan Walsh <dwalsh@redhat.com> 1.4-2
- Fix install locations of policy_src_dir

* Wed Jun 2 2004 Dan Walsh <dwalsh@redhat.com> 1.4-1
- Update to latest from TRESYS.

* Tue Jun 1 2004 Dan Walsh <dwalsh@redhat.com> 1.3-3
- Make changes to work with targeted/strict policy
* Fri Apr 16 2004 Dan Walsh <dwalsh@redhat.com> 1.3-2
- Take out requirement for policy file

* Fri Apr 16 2004 Dan Walsh <dwalsh@redhat.com> 1.3-1
- Fix doc location

* Fri Apr 16 2004 Dan Walsh <dwalsh@redhat.com> 1.3-1
- Latest from TRESYS

* Tue Apr 13 2004 Dan Walsh <dwalsh@redhat.com> 1.2.1-8
- fix location of policy.conf file

* Tue Apr 6 2004 Dan Walsh <dwalsh@redhat.com> 1.2.1-7
- Obsolete setools-devel
* Tue Apr 6 2004 Dan Walsh <dwalsh@redhat.com> 1.2.1-6
- Fix location of 
* Tue Apr 6 2004 Dan Walsh <dwalsh@redhat.com> 1.2.1-5
- Remove devel libraries
- Fix installdir for lib64

* Sat Apr 3 2004 Dan Walsh <dwalsh@redhat.com> 1.2.1-4
- Add usr_t file read to policy

* Thu Mar 25 2004 Dan Walsh <dwalsh@redhat.com> 1.2.1-3
- Use tcl8.4

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 6 2004 Dan Walsh <dwalsh@redhat.com> 1.2.1-1
- New patch

* Fri Feb 6 2004 Dan Walsh <dwalsh@redhat.com> 1.2-1
- Latest upstream version

* Tue Dec 30 2003 Dan Walsh <dwalsh@redhat.com> 1.1.1-1
- New version from upstream
- Remove seuser.te.  Now in policy file.

* Tue Dec 30 2003 Dan Walsh <dwalsh@redhat.com> 1.1-2
- Add Defattr to devel
- move libs to base kit

* Fri Dec 19 2003 Dan Walsh <dwalsh@redhat.com> 1.1-1
- Update to latest code from tresys
- Break into three separate packages for cmdline, devel and gui
- Incorporate the tcl patch

* Mon Dec 15 2003 Jens Petersen <petersen@redhat.com> - 1.0.1-3
- apply setools-1.0.1-tcltk.patch to build against tcl/tk 8.4
- buildrequire tk-devel

* Thu Nov 20 2003 Dan Walsh <dwalsh@redhat.com> 1.0.1-2
- Add Bwidgets to this RPM

* Tue Nov 4 2003 Dan Walsh <dwalsh@redhat.com> 1.0.1-1
- Upgrade to 1.0.1

* Wed Oct 15 2003 Dan Walsh <dwalsh@redhat.com> 1.0-6
- Clean up build

* Tue Oct 14 2003 Dan Walsh <dwalsh@redhat.com> 1.0-5
- Update with correct seuser.te

* Wed Oct 1 2003 Dan Walsh <dwalsh@redhat.com> 1.0-4
- Update with final release from Tresys

* Mon Jun 2 2003 Dan Walsh <dwalsh@redhat.com> 1.0-1
- Initial version
