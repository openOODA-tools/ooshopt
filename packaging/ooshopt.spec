Name:           ooshopt
Version:        0.1.0
Release:        1%{?dist}
Summary:        Declarative kernel and userland shell options toggling strict evaluation and trace modes.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooshopt
Source0:        ooshopt-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooshopt is a sovereign, capability-bounded SHELL TUNER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooshopt
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooshopt-uninstall

%files
/usr/bin/ooshopt
/usr/bin/ooshopt-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
