%define debug_package %{nil}

Summary: StotinkaOS Xfce defaults configs
Name:    stotinkaos-xfce-defaults
Version: 0.1
Release: 1%{?dist}
Group:   System Environment/Base
License: GPLv3+
Url:     http://stotinkaos.net/
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: google-noto-sans-fonts google-noto-serif-fonts google-droid-sans-mono-fonts
Requires: faba-icon-theme faba-mono-icons moka-icon-theme
BuildArch: noarch

%description
%{summary}.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_sysconfdir}/skel/.config

cp -a %{_builddir}/%{name}-%{version}/xfce4 %{buildroot}%{_sysconfdir}/skel/.config/

%clean
rm -rf %{buildroot}

%pre

%post

%files
%defattr(-,root,root)
%{_sysconfdir}/skel/.config/xfce4

%changelog
* Sat Jul 23 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 0.1-1
- initial "build"
