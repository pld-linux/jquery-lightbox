# TODO
# - demo package
%define		plugin	lightbox
Summary:	jQuery lightbox plugin
Name:		jquery-%{plugin}
Version:	0.5
Release:	2
License:	BSD
Group:		Applications/WWW
Source0:	https://github.com/downloads/krewenki/jquery-lightbox/jquery-lightbox.zip
# Source0-md5:	b374adbfd69b1b484b6876fb4872b125
URL:		http://krewenki.github.com/jquery-lightbox/
BuildRequires:	closure-compiler
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
BuildRequires:	yuicompressor
Requires:	jquery >= 1.2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
jQuery Lightbox is a simple port of the popular lightbox script, which
is based on prototype and scriptaculous, to jQuery.

%prep
%setup -qn %{name}

%{__sed} -i -e 's,\.\./images/,images/,g' css/*.css

%build
install -d build/css

# compress .js
js=jquery.%{plugin}.js
out=build/$js
%if 0%{!?debug:1}
closure-compiler --js $js --charset UTF-8 --js_output_file $out
js -C -f $out
%else
cp -p $js $out
%endif

%if 0%{!?debug:1}
css=css/%{plugin}.css
# compress with yui to get rid of comments, etc
yuicompressor --charset UTF-8 $css -o build/$css
%else
cp -p $css build/$css
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p build/jquery.%{plugin}.js  $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
cp -p build/css/%{plugin}.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}.css
cp -a images $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.markdown
%{_appdir}
