#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-vcr
Version  : 0.3.0
Release  : 17
URL      : https://cran.r-project.org/src/contrib/vcr_0.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/vcr_0.3.0.tar.gz
Summary  : Record 'HTTP' Calls to Disk
Group    : Development/Tools
License  : MIT
Requires: R-R6
Requires: R-base64enc
Requires: R-crul
Requires: R-httr
Requires: R-lazyeval
Requires: R-urltools
Requires: R-webmockr
Requires: R-yaml
BuildRequires : R-R6
BuildRequires : R-base64enc
BuildRequires : R-crul
BuildRequires : R-httr
BuildRequires : R-lazyeval
BuildRequires : R-urltools
BuildRequires : R-webmockr
BuildRequires : R-yaml
BuildRequires : buildreq-R

%description
vcr
===
[![cran checks](https://cranchecks.info/badges/worst/vcr)](https://cranchecks.info/pkgs/vcr)
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
[![Build Status](https://travis-ci.org/ropensci/vcr.svg)](https://travis-ci.org/ropensci/vcr)
[![Build status](https://ci.appveyor.com/api/projects/status/6sewc0t3bhdg5opo?svg=true)](https://ci.appveyor.com/project/sckott/vcr)
[![codecov](https://codecov.io/gh/ropensci/vcr/branch/master/graph/badge.svg)](https://codecov.io/gh/ropensci/vcr)
[![rstudio mirror downloads](http://cranlogs.r-pkg.org/badges/vcr)](https://github.com/metacran/cranlogs.app)
[![cran version](https://www.r-pkg.org/badges/version/vcr)](https://cran.r-project.org/package=vcr)

%prep
%setup -q -c -n vcr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1566487145

%install
export SOURCE_DATE_EPOCH=1566487145
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library vcr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library vcr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library vcr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/vcr/DESCRIPTION
/usr/lib64/R/library/vcr/INDEX
/usr/lib64/R/library/vcr/LICENSE
/usr/lib64/R/library/vcr/Meta/Rd.rds
/usr/lib64/R/library/vcr/Meta/data.rds
/usr/lib64/R/library/vcr/Meta/features.rds
/usr/lib64/R/library/vcr/Meta/hsearch.rds
/usr/lib64/R/library/vcr/Meta/links.rds
/usr/lib64/R/library/vcr/Meta/nsInfo.rds
/usr/lib64/R/library/vcr/Meta/package.rds
/usr/lib64/R/library/vcr/Meta/vignette.rds
/usr/lib64/R/library/vcr/NAMESPACE
/usr/lib64/R/library/vcr/NEWS.md
/usr/lib64/R/library/vcr/R/vcr
/usr/lib64/R/library/vcr/R/vcr.rdb
/usr/lib64/R/library/vcr/R/vcr.rdx
/usr/lib64/R/library/vcr/data/Rdata.rdb
/usr/lib64/R/library/vcr/data/Rdata.rds
/usr/lib64/R/library/vcr/data/Rdata.rdx
/usr/lib64/R/library/vcr/doc/configuration.R
/usr/lib64/R/library/vcr/doc/configuration.Rmd
/usr/lib64/R/library/vcr/doc/configuration.html
/usr/lib64/R/library/vcr/doc/index.html
/usr/lib64/R/library/vcr/doc/request_matching.R
/usr/lib64/R/library/vcr/doc/request_matching.Rmd
/usr/lib64/R/library/vcr/doc/request_matching.html
/usr/lib64/R/library/vcr/doc/vcr.R
/usr/lib64/R/library/vcr/doc/vcr.Rmd
/usr/lib64/R/library/vcr/doc/vcr.html
/usr/lib64/R/library/vcr/help/AnIndex
/usr/lib64/R/library/vcr/help/aliases.rds
/usr/lib64/R/library/vcr/help/paths.rds
/usr/lib64/R/library/vcr/help/vcr.rdb
/usr/lib64/R/library/vcr/help/vcr.rdx
/usr/lib64/R/library/vcr/html/00Index.html
/usr/lib64/R/library/vcr/html/R.css
/usr/lib64/R/library/vcr/tests/test-all.R
/usr/lib64/R/library/vcr/tests/testthat/helper-vcr.R
/usr/lib64/R/library/vcr/tests/testthat/httr_obj.rda
/usr/lib64/R/library/vcr/tests/testthat/test-Cassette.R
/usr/lib64/R/library/vcr/tests/testthat/test-Filesystem.R
/usr/lib64/R/library/vcr/tests/testthat/test-HttpInteraction.R
/usr/lib64/R/library/vcr/tests/testthat/test-HttpInteractionList.R
/usr/lib64/R/library/vcr/tests/testthat/test-Persisters.R
/usr/lib64/R/library/vcr/tests/testthat/test-RequestHandler.R
/usr/lib64/R/library/vcr/tests/testthat/test-RequestMatcherRegistry.R
/usr/lib64/R/library/vcr/tests/testthat/test-ause_cassette.R
/usr/lib64/R/library/vcr/tests/testthat/test-ause_cassette_match_requests_on.R
/usr/lib64/R/library/vcr/tests/testthat/test-ause_cassette_re_record.R
/usr/lib64/R/library/vcr/tests/testthat/test-ause_cassette_record_modes.R
/usr/lib64/R/library/vcr/tests/testthat/test-cassette_options.R
/usr/lib64/R/library/vcr/tests/testthat/test-cassettes.R
/usr/lib64/R/library/vcr/tests/testthat/test-eject_cassette.R
/usr/lib64/R/library/vcr/tests/testthat/test-errors.R
/usr/lib64/R/library/vcr/tests/testthat/test-httr.R
/usr/lib64/R/library/vcr/tests/testthat/test-insert_cassette.R
/usr/lib64/R/library/vcr/tests/testthat/test-lightswitch.R
/usr/lib64/R/library/vcr/tests/testthat/test-logger.R
/usr/lib64/R/library/vcr/tests/testthat/test-no-cassette-in-use.R
/usr/lib64/R/library/vcr/tests/testthat/test-request_summary.R
/usr/lib64/R/library/vcr/tests/testthat/test-use_vcr.R
/usr/lib64/R/library/vcr/tests/testthat/test-write_interactions.R
