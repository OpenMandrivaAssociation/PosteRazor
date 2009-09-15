%define name PosteRazor
%define version 1.5
%define release %mkrel 5

Name:           %{name} 
Summary:        PosteRazor cuts a raster image into pieces
Version:        %{version} 
Release:        %{release} 
Source0:        %{name}-%{version}-Source.tar.bz2
Patch0:		FlPosteRazorHelpDialog.patch
Patch1:		FlPosteRazorSpinner.patch

URL:            http://posterazor.sourceforge.net 
Group:          Graphics 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	cmake
BuildRequires:	freeimage-devel
BuildRequires:	xpm-devel
BuildRequires:	fltk-devel
BuildRequires:	xft2-devel
License:        GPLv3+

%description
PosteRazor takes a raster image. The resulting poster is saved as a 
multipage PDF document. An easy to use, wizard like user interface 
guides through 5 steps. PosteRazor is available as a Windows, an OSX
and a Linux version. It is an open source, GNU licensed project which
is hosted on SourceForge.net.

%prep
%setup -q -n %{name}-%{version}
rm -rf packaging
%patch0
%patch1

%build
cd src
%cmake
%make

%install
rm -fr %buildroot
cd src/build
install -D -m755 PosteRazor $RPM_BUILD_ROOT/%{_bindir}/PosteRazor

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES LICENSE README
%{_bindir}/*
