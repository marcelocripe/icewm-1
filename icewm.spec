%define name		    icewm
%define version		    1.0.9
%define release		    2
%define group		    X11/Window Managers

%define prefix		    %{_usr}
%define exec_prefix	    %{_usr}/X11R6
%define sysconfdir	    %{_sysconfdir}
%define bindir		    %{exec_prefix}/bin/
%define libdir		    %{exec_prefix}/lib/X11/icewm/
%define locdir		    %{prefix}/share/locale/
%define docdir		    %{_docdir}

%define lite_apps	    icewm icesh icewmbg icewmhint
%define default_apps	    icewm icesh icewmbg icewmhint icehelp
%define gnome_apps	    icewm icesh icewmbg icewmhint icehelp icesound
%define experimental_apps   icewm icesh icewmbg icewmhint icehelp icesound
%define all_apps	    icewm icesh icewmbg icewmhint icehelp icesound

%define icewm_docroot       %{docdir}/%{name}-%{version}
%define redhat_docroot      %{docdir}/%{name}-common-%{version}
%define suse_docroot        %{docdir}/%{name}-common

# ==============================================================================

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	X11 Window Manager
Group:		%{group}
License:	LGPL
URL:		http://www.icewm.org/
Packager:       Mathias Hasselmann <mathias.hasselmann@gmx.de>
Source:		http://download.sourceforge.net/icewm/%{name}-%{version}-%{release}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Window Manager for X Window System. Can emulate the look of Windows'95, OS/2
Warp 3,4, Motif or the Java Metal GUI. Tries to take the best features of the
above systems. Features multiple workspaces, opaque move/resize, task bar,
window list, mailbox status, digital clock. Fast and small.

%ifarch noarch # =============================================== noarch part ===

%package -n %{name}-common
Summary:	X11 Window Manager
Group:		%{group}
#Requires:       %{name}-bin = %{version}-%{release}

%description -n %{name}-common
Window Manager for X Window System. Can emulate the look of Windows'95, OS/2
Warp 3,4, Motif or the Java Metal GUI. Tries to take the best features of the
above systems. Features multiple workspaces, opaque move/resize, task bar,
window list, mailbox status, digital clock. Fast and small.

This package provides the necessary data files. To make this package useful,
you have to install one of the binary packages: %{name}-lite, %{name}-default,
%{name}-gnome or %{name}-experimental.

%prep
%setup -D -T

%build
pushd default/%{name}-%{version} # --------------------- build documentation ---
  make docs icewm.lsm
popd

%install
pushd default/%{name}-%{version} # --- install documentation and common data ---
  make install \
    prefix=$RPM_BUILD_ROOT%{prefix} \
    exec_prefix=$RPM_BUILD_ROOT%{exec_prefix} \
    sysconfdir=$RPM_BUILD_ROOT%{sysconfdir} \
    DOCDIR=$RPM_BUILD_ROOT%{docdir}
popd

%post -n %{name}-common
rm -fr %{icewm_docroot}
( test -d %{redhat_docroot} && ln -s %{redhat_docroot} %{icewm_docroot} ) ||
( test -d %{suse_docroot} && ln -s %{suse_docroot} %{icewm_docroot} )

%preun -n %{name}-common
rm -fr %{icewm_docroot}

%files -n %{name}-common
%defattr(-,root,root)
%doc README COPYING AUTHORS CHANGES TODO BUGS FAQ* doc/*.html doc/icewm.sgml
%doc default/%{name}-%{version}/icewm.lsm

%config %{libdir}/keys
%config %{libdir}/menu
%config %{libdir}/preferences
%config %{libdir}/toolbar
%config %{libdir}/winoptions

%dir %{libdir}/icons
%dir %{libdir}/ledclock
%dir %{libdir}/mailbox
%dir %{libdir}/taskbar
%dir %{libdir}/themes
%dir %{locdir}

%{libdir}/icons/*
%{libdir}/ledclock/*
%{libdir}/mailbox/*
%{libdir}/taskbar/*
%{libdir}/themes/*
%{locdir}/*

%else # ======================================================== binary part ===

%package -n %{name}-default
Summary:	The default version of IceWM
Group:		%{group}
Requires:       %{name}-common = %{version}-%{release}
Provides:       %{name}-bin = %{version}-%{release}
Conflicts:      %{name}-experimental, %{name}-gnome, %{name}-lite

%description -n %{name}-default
Window Manager for X Window System. Can emulate the look of Windows'95, OS/2
Warp 3,4, Motif or the Java Metal GUI. Tries to take the best features of the
above systems. Features multiple workspaces, opaque move/resize, task bar,
window list, mailbox status, digital clock. Fast and small.

This version is compiled with nothing but the default settings (including
support for GNOME Window Manager hints).

%package lite
Summary:	A very lightweight version of IceWM
Group:		%{group}
Requires:       %{name}-common = %{version}-%{release}
Provides:       %{name}-bin = %{version}-%{release}
Conflicts:      %{name}-experimental, %{name}-gnome, %{name}-default

%description lite
Window Manager for X Window System. Can emulate the look of Windows'95, OS/2
Warp 3,4, Motif or the Java Metal GUI. Tries to take the best features of the
above systems. Features multiple workspaces, opaque move/resize, task bar,
window list, mailbox status, digital clock. Fast and small.

This is the lite version with minimal features. There is no support for
virtual workspaces. The entire taskbar, the window list/menu, tooltips are
disabled.


%package gnome
Summary:	The GNOME version of IceWM
Group:		%{group}
Requires:       %{name}-common = %{version}-%{release}, imlib, gnome-libs
Provides:       %{name}-bin = %{version}-%{release}
Conflicts:      %{name}-experimental, %{name}-lite, %{name}-default

%description gnome
Window Manager for X Window System. Can emulate the look of Windows'95, OS/2
Warp 3,4, Motif or the Java Metal GUI. Tries to take the best features of the
above systems. Features multiple workspaces, opaque move/resize, task bar,
window list, mailbox status, digital clock. Fast and small.

This is the GNOME version with all the necessary features build in. Main
difference to the default version is usage of the Imlib library for image
handling and support for GNOME/KDE application menus.

%package experimental
Summary:	An experimental version of IceWM
Group:		%{group}
Requires:       %{name}-common = %{version}-%{release}, imlib, gnome-libs
Provides:       %{name}-bin = %{version}-%{release}
Conflicts:      %{name}-gnome, %{name}-lite, %{name}-default

%description experimental
Window Manager for X Window System. Can emulate the look of Windows'95, OS/2
Warp 3,4, Motif or the Java Metal GUI. Tries to take the best features of the
above systems. Features multiple workspaces, opaque move/resize, task bar,
window list, mailbox status, digital clock. Fast and small.

This is the experimental version of IceWM. It contains all the features of 
the GNOME version and some additional experimental features. Those
experimental features include enhanced move/size effects, antialiasing,
grandients and shaped window decorations.

%prep
%setup -q

for i in default lite gnome experimental; do
  mkdir -p ${i} && pushd ${i} && bzip2 -dc %{SOURCE0} | tar xf - && popd
done

%build
pushd default/%{name}-%{version} # --------------- build the default version ---
  CXXFLAGS="$RPM_OPT_FLAGS" ./configure \
    --prefix=%{prefix} --exec-prefix=%{exec_prefix} --sysconfdir=%{sysconfdir} \
     --with-docdir=%{docdir} --disable-debug --enable-i18n --enable-nls \
    --disable-guievents --without-gnome-menus --with-xpm
  make
popd

pushd lite/%{name}-%{version} # --------------------- build the lite version ---
  CXXFLAGS="$RPM_OPT_FLAGS" ./configure \
    --prefix=%{prefix} --exec-prefix=%{exec_prefix} --sysconfdir=%{sysconfdir} \
    --with-docdir=%{docdir} --disable-debug --enable-lite \
    --disable-i18n --disable-nls --disable-guievents --disable-xfreetype \
    --disable-sm --without-gnome-menus --with-xpm
  make
popd

pushd gnome/%{name}-%{version} # ------------------- build the GNOME version ---
  { CXXFLAGS="$RPM_OPT_FLAGS" ./configure \
      --prefix=%{prefix} --exec-prefix=%{exec_prefix} \
      --sysconfdir=%{sysconfdir} --with-docdir=%{docdir} \
      --disable-debug --enable-i18n --enable-nls --enable-guievents \
      --with-icesound=oss,esd --with-gnome-menus --with-imlib && \
    make
  } || { \
    echo WARNING: Creating stub scripts because GNOME is not available.
    for stub in %{gnome_apps}; do
      cat >> src/$stub <<.
#!/bin/sh

cat <<+
The GNOME version of $stub %{version} was not compiled because
no development packages of GNOME were installed on `hostname -f`
building this RPM package.

Try to install the default binary package or the rebuild the
gnome package on a system having the GNOME development packages
installed.
+
.
      chmod a+x src/$stub
    done
  }
popd

pushd experimental/%{name}-%{version} # ----- build the experimental version ---
  { CXXFLAGS="$RPM_OPT_FLAGS" ./configure \
      --prefix=%{prefix} --exec-prefix=%{exec_prefix} \
      --sysconfdir=%{sysconfdir} --with-docdir=%{docdir} \
      --disable-debug --enable-i18n --enable-nls --enable-guievents \
      --with-icesound=oss,esd --with-gnome-menus --with-imlib \
      --enable-movesize-fx --enable-antialiasing --enable-xfreetype \
      --enable-gradients --enable-shaped-decorations && \
    make
  } || { \
    echo WARNING: Creating stub scripts because GNOME is not available.
    for stub in %{experimental_apps}; do
      cat >> src/$stub <<.
#!/bin/sh

cat <<+
The GNOME version of $stub %{version} was not compiled because
no development packages of GNOME were installed on `hostname -f`
building this RPM package.

Try to install the default binary package or the rebuild the
experimental package on a system having the GNOME development
packages installed.
+
.
      chmod a+x src/$stub
    done
  }
popd

# ------------------------------------------------- build the noarch package ---
rpm -bb --target=noarch-%{_vendor}-%{_os} icewm.spec

%install
# ---------------------------- rename the binaries to ${basename}-${variant} ---
for app in %{all_apps}; do
  rm -f $RPM_BUILD_ROOT%{bindir}/${app}
done

for variant in default lite gnome experimental; do
  for binary in %{all_apps}; do
    cp ${variant}/%{name}-%{version}/src/${binary} \
    	$RPM_BUILD_ROOT%{bindir}${binary}-${variant} || :
  done
done

# --------------- create symlinks from ${basename}-${variant} to ${basename} ---
%post -n %{name}-default
for bin in %{default_apps}; do 
    rm -f %{bindir}${bin}
    ln -s ${bin}-default %{bindir}${bin}
done
%postun -n %{name}-default
test "$1" = 0 && for bin in %{default_apps}; do 
    rm -f %{bindir}${bin}
done

%post lite
for bin in %{lite_apps}; do 
    rm -f %{bindir}${bin}
    ln -s ${bin}-lite %{bindir}${bin}
done
%postun lite
test "$1" = 0 && for bin in %{lite_apps}; do 
    rm -f %{bindir}${bin}
done

%post gnome
for bin in %{gnome_apps}; do 
    rm -f %{bindir}${bin}
    ln -s ${bin}-gnome %{bindir}${bin}
done
%postun gnome
test "$1" = 0 && for bin in %{gnome_apps}; do 
    rm -f %{bindir}${bin}
done

%post experimental
for bin in %{experimental_apps}; do 
    rm -f %{bindir}${bin}
    ln -s ${bin}-experimental %{bindir}${bin}
done
%postun experimental
test "$1" = 0 && for bin in %{experimental_apps}; do 
    rm -f %{bindir}${bin}
done


# --------------------------------------------------------------- file lists ---
%files -n %{name}-default
%defattr(-,root,root)
%{bindir}*-default

%files lite
%defattr(-,root,root)
%{bindir}*-lite

%files gnome
%defattr(-,root,root)
%{bindir}*-gnome

%files experimental
%defattr(-,root,root)
%{bindir}*-experimental

# ------------------------------------------------------------------ cleanup ---
%clean
test -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != "/" && rm -rf $RPM_BUILD_ROOT

%endif # ============================================================== tail ===

%changelog
* Mon Oct 08 2001 Mathias Hasselmann <mathias.hasselmann@gmx.de>
- try to respect SuSE's idea of the documentation location

* Mon Sep 26 2001 Mathias Hasselmann <mathias.hasselmann@gmx.de> 1.0.9-pre2
- fixed configure flags for lite version
- added experimental package

* Mon Aug 08 2001 Mathias Hasselmann <mathias.hasselmann@gmx.de> 1.0.9-pre1
- added License tag since Copyright is deprecated

* Mon May 07 2001 Mathias Hasselmann <mathias.hasselmann@gmx.de> 1.0.8-6
- icewm-default was missed to call make
  -> icewm compiled by %install
  -> binaries contained invalid paths

* Mon Apr 02 2001 Mathias Hasselmann <mathias.hasselmann@gmx.de> 1.0.8-3
- allow to rebuild on systems without GNOME
- removed the virtual icewm-bin from icewm-common
- marked menu, toolbar, keys, preferences and winoptions as %config files

* Fri Mar 23 2001 Mathias Hasselmann <mathias.hasselmann@gmx.de> 1.0.8-1
- move the docs from icewm-common-%{version} to icewm-%{version}
- cleaned (post) installation scripts

* Sun Mar 04 2001 Mathias Hasselmann <mathias.hasselmann@gmx.de> 1.0.7-3
- some icehelp trouble

* Fri Feb 16 2001 Pavel Roskin <proski@gnu.org> 1.0.7-2
- fixed the bash2 problem

* Sat Jan 27 2001 Mathias Hasselmann <mathias.hasselmann@gmx.de> 1.0.7-1
- added icehelp and icesound

* Sat Jan 14 2001 Mathias Hasselmann <mathias.hasselmann@gmx.de> 1.0.6-4
- last minute feature: shadowed title bars

* Fri Jan 12 2001 Mathias Hasselmann <mathias.hasselmann@gmx.de> 1.0.6-3
- renamed again: icewm-common-VERSION-RELEASE.noarch.rpm and
  icewm-{default,lite,gnome}-VERSION-RELEASE.ARCH.rpm
- noarch.rpm is built recursively by the src.rpm
- support for docdir (Mandrake)

* Mon Jan  8 2001 Mathias Hasselmann <mathias.hasselmann@gmx.de> 1.0.6-2
- translated messages weren't packaged
- new macros: bindir, libdir, localedir

* Mon Jan  8 2001 Mathias Hasselmann <mathias.hasselmann@gmx.de> 1.0.6-1
- "Backported" to RPM3 (%make variable)
- icewm.lsm was not packaged
- changed icewm-{lite,default,gnome} to icewm-{lite,default,gnome} to
  avoid confusion
- extended default description

* Thu Jan  4 2001 Alexander Skwar <ASkwar@DigitalProjects.com> 1.0.5-1
- Completely rewrote spec file to do away with needing
  three different src.rpm's
