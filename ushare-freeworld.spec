Summary: UPnP (TM) A/V & DLNA Media Server
Name: ushare-freeworld
Version: 1.1a
Release: 6%{?dist}
License: LGPLv2+
Group: Applications/Multimedia
URL: http://ushare.geexbox.org/

Source: http://ushare.geexbox.org/releases/ushare-%{version}.tar.bz2
Patch0: ushare-error.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: libupnp-devel, pkgconfig, libdlna-devel
Requires: ushare >= %{version}
Requires(post): /usr/sbin/alternatives
Requires(preun): /usr/sbin/alternatives
Requires(postun): /sbin/service

%description
uShare is a UPnP (TM) A/V & DLNA Media Server. It implements the server 
component that provides UPnP media devices with information on 
available multimedia files. uShare uses the built-in http server 
of libupnp to stream the files to clients.


%prep
%setup -q -n ushare-%{version}
%patch0 -p1

%build
export CFLAGS="$RPM_OPT_FLAGS"
./configure --prefix=%{_prefix} --localedir=%{_datadir}/locale --sysconfdir=%{_sysconfdir} --enable-dlna --enable-debug

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%{__install} -pm 0755 -D src/ushare %{buildroot}%{_bindir}/ushare-freeworld

%clean
rm -rf %{buildroot}

%post
alternatives --install %{_bindir}/ushare ushare %{_bindir}/ushare-freeworld 20
service ushare condrestart &>/dev/null || :

%preun
if [ $1 -eq 0 ]; then
alternatives --remove ushare %{_bindir}/ushare-freeworld
service ushare condrestart &>/dev/null || :
fi

%postun
if [ $1 -ge 1 ]; then
	service ushare condrestart &>/dev/null || :
fi

%files
%{_bindir}/ushare-freeworld

%changelog
* Sat Dec 20 2008 Dominik Mierzejewski <rpm@greysector.net> - 1.1a-6
- rebuild against new ffmpeg

* Sun Aug 03 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 1.1a-5
- rebuild

* Sun Mar 09 2008 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.1a-4
- BZ 436607

* Fri Jan 25 2008 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.1a-3
- Correct some spec error

* Tue Dec 25 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.1a-2
- Correct some spec error

* Wed Dec 05 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.1a-1
- Update to 1.1a

* Sun Nov 18 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.0-4
- Rebuild for new libupnp.

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.0-2
- Rebuild for selinux ppc32 issue.

* Fri Jul 06 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.0-1
- Update to 1.0

* Tue Jun 26 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.9.10-4
- Rebuild

* Sat May 05 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.9.10-3
- Rebuild for libupnp-1.6.0

* Sat May 05 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.9.10-2
- Rebuild

* Mon Feb 26 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.9.10-1
- Update to 0.9.10

* Sun Feb 25 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.9.9-1
- Update to 0.9.9

* Sat Feb 17 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.9.8-2
- Rebuild for libupnp 1.4.2

* Wed Dec 13 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.9.8-1
- Update to 0.9.8

* Thu Jun 29 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.9.7-2
- Add pkgconfig to buildrequires

* Sun Mar 12 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.9.7-1
- Update to 0.9.7

* Tue Feb 14 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.9.6-1
- Update to 0.9.6

* Tue Feb 14 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.9.5-6
- Rebuild for FC5

* Fri Feb 10 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.9.5-5
- Rebuild for FC5

* Tue Dec 27 2005 Eric Tanguy 0.9.5-4
- Use %find_lang macro instead of %{_datadir}/locale/*

* Tue Dec 27 2005 Eric Tanguy 0.9.5-3
- Drop "Requires: libupnp"
- replace %{_sysconfdir}/ushare.conf by %config(noreplace) %{_sysconfdir}/ushare.conf

* Tue Dec 27 2005 Eric Tanguy 0.9.5-2
- add patch for buffer

* Tue Dec 27 2005 Eric Tanguy 0.9.5-1
- First build
