# TODO
# - demo package
%define		plugin	lightbox
Summary:	jQuery lightBox plugin
Name:		jquery-%{plugin}
Version:	0.5
Release:	1
License:	CC Attribution SA 2.5
Group:		Applications/WWW
Source0:	http://leandrovieira.com/projects/jquery/lightbox/releases/jquery-lightbox-%{version}.zip
# Source0-md5:	6ea2479de1e85b45993c1cfa9bacf15f
URL:		http://leandrovieira.com/projects/jquery/lightbox
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	yuicompressor
Requires:	jquery >= 1.2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
jQuery lightBox plugin is simple, elegant, unobtrusive, no need extra
markup and is used to overlay images on the current page through the
power and flexibility of jQuery's selector.

lightBox is a plugin for jQuery. It was inspired in Lightbox JS by
Lokesh Dhakar.

%prep
%setup -qc

%build
install -d build/css
css=css/jquery.lightbox-0.5.css
yuicompressor --charset UTF-8 --type css $css -o build/$css

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p js/jquery.%{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p js/jquery.%{plugin}-%{version}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
cp -p build/css/jquery.%{plugin}-%{version}.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}.css

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
