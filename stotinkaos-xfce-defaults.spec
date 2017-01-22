%define debug_package %{nil}

Summary: StotinkaOS Xfce defaults configs
Name:    stotinkaos-xfce-defaults
Version: 0.2
Release: 1%{?dist}
Group:   System Environment/Base
License: GPLv3+
Url:     http://stotinkaos.net/
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: google-noto-sans-fonts google-noto-serif-fonts google-droid-sans-mono-fonts
Requires: faba-icon-theme faba-mono-icons moka-icon-theme
Requires: freetype-freeworld
Requires(post): glib2
BuildArch: noarch

%description
%{summary}.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_sysconfdir}/skel/.config
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
mkdir -p %{buildroot}%{_sysconfdir}/skel
mkdir -p %{buildroot}%{_sysconfdir}/fonts
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas

install -m 0755 %{_builddir}/%{name}-%{version}/nanorc %{buildroot}%{_sysconfdir}/skel/.nanorc
cp -a %{_builddir}/%{name}-%{version}/Templates %{buildroot}%{_sysconfdir}/skel/
install -m 0755 %{_builddir}/%{name}-%{version}/kern_dir.sh %{buildroot}%{_sysconfdir}/profile.d/kern_dir.sh
install -m 0755 %{_builddir}/%{name}-%{version}/color_prompt.sh %{buildroot}%{_sysconfdir}/profile.d/color_prompt.sh
install -m 0755 %{_builddir}/%{name}-%{version}/local.conf %{buildroot}%{_sysconfdir}/fonts/local.conf
install -m 0644 %{_builddir}/%{name}-%{version}/org.stotinkaos.gschema.override %{buildroot}%{_datadir}/glib-2.0/schemas/org.stotinkaos.gschema.override
cp -a %{_builddir}/%{name}-%{version}/xfce4 %{buildroot}%{_sysconfdir}/skel/.config/

%clean
rm -rf %{buildroot}

%post
# rebuild schema cache with any overrides we installed
glib-compile-schemas /usr/share/glib-2.0/schemas 2>/dev/null

%postun
# rebuild schema cache with any overrides we installed
glib-compile-schemas /usr/share/glib-2.0/schemas 2>/dev/null

%files
%defattr(-,root,root)
%{_sysconfdir}/skel/.nanorc
%{_sysconfdir}/skel/Templates/*
%{_sysconfdir}/profile.d/kern_dir.sh
%{_sysconfdir}/profile.d/color_prompt.sh
%{_sysconfdir}/fonts/local.conf
%{_datadir}/glib-2.0/schemas/org.stotinkaos.gschema.override
%{_sysconfdir}/skel/.config/xfce4

%changelog
* Tue Dec 27 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 0.2-1
- add missing helpers.rc
* Sat Jul 23 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 0.1-1
- initial "build"
