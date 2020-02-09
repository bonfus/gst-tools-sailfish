# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       gst-tools
Summary:    Gstreamer tools for Sailfish
Version:    1.0
Release:    1
Group:      Qt/Qt
License:    GPL
URL:        http://example.org/
Source0:    %{name}-%{version}.tar.bz2
Source100:  gst-tools.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.0.2
BuildRequires:  cmake


%description
This sample project shows how to build a Sailfish application with a
custom build system



%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
rm -rf rpmbuilddir
mkdir rpmbuilddir
cd rpmbuilddir &&  cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_INSTALL_PREFIX=/usr ..
cd ..
make -C rpmbuilddir -j VERBOSE=1 %{?_smp_mflags}
# << build pre



# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
DESTDIR=%{buildroot} make -C rpmbuilddir install
mkdir -p %{_bindir}
# << install pre



%files
%defattr(-,root,root,-)
%{_bindir}
# >> files
# << files

