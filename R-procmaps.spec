#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-procmaps
Version  : 0.0.4
Release  : 11
URL      : https://cran.r-project.org/src/contrib/procmaps_0.0.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/procmaps_0.0.4.tar.gz
Summary  : Portable Address Space Mapping
Group    : Development/Tools
License  : BSD-3-Clause GPL-3.0
Requires: R-procmaps-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
Determine which library or other region is mapped to a specific
    address of a process. --
    R packages can contain native code, compiled to shared libraries at build or
    installation time.
    When loaded, each shared library occupies a portion of the address space of
    the main process.
    When only a machine instruction pointer is available (e.g. from a backtrace
    during error inspection or profiling), the address space map determines
    which library this instruction pointer corresponds to.

%package lib
Summary: lib components for the R-procmaps package.
Group: Libraries

%description lib
lib components for the R-procmaps package.


%prep
%setup -q -c -n procmaps
cd %{_builddir}/procmaps

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633359928

%install
export SOURCE_DATE_EPOCH=1633359928
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library procmaps
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library procmaps
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library procmaps
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc procmaps || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/procmaps/DESCRIPTION
/usr/lib64/R/library/procmaps/INDEX
/usr/lib64/R/library/procmaps/Meta/Rd.rds
/usr/lib64/R/library/procmaps/Meta/features.rds
/usr/lib64/R/library/procmaps/Meta/hsearch.rds
/usr/lib64/R/library/procmaps/Meta/links.rds
/usr/lib64/R/library/procmaps/Meta/nsInfo.rds
/usr/lib64/R/library/procmaps/Meta/package.rds
/usr/lib64/R/library/procmaps/NAMESPACE
/usr/lib64/R/library/procmaps/NEWS.md
/usr/lib64/R/library/procmaps/R/procmaps
/usr/lib64/R/library/procmaps/R/procmaps.rdb
/usr/lib64/R/library/procmaps/R/procmaps.rdx
/usr/lib64/R/library/procmaps/WORDLIST
/usr/lib64/R/library/procmaps/help/AnIndex
/usr/lib64/R/library/procmaps/help/aliases.rds
/usr/lib64/R/library/procmaps/help/paths.rds
/usr/lib64/R/library/procmaps/help/procmaps.rdb
/usr/lib64/R/library/procmaps/help/procmaps.rdx
/usr/lib64/R/library/procmaps/html/00Index.html
/usr/lib64/R/library/procmaps/html/R.css
/usr/lib64/R/library/procmaps/tests/output.R
/usr/lib64/R/library/procmaps/tests/testthat.R
/usr/lib64/R/library/procmaps/tests/testthat/test-get.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/procmaps/libs/procmaps.so
