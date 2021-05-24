#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-vcr
Version  : 1.0.0
Release  : 32
URL      : https://cran.r-project.org/src/contrib/vcr_1.0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/vcr_1.0.0.tar.gz
Summary  : Record 'HTTP' Calls to Disk
Group    : Development/Tools
License  : MIT
Requires: R-vcr-lib = %{version}-%{release}
Requires: R-R6
Requires: R-base64enc
Requires: R-cpp11
Requires: R-crul
Requires: R-httr
Requires: R-rprojroot
Requires: R-urltools
Requires: R-webmockr
Requires: R-yaml
BuildRequires : R-R6
BuildRequires : R-base64enc
BuildRequires : R-cpp11
BuildRequires : R-crul
BuildRequires : R-httr
BuildRequires : R-rprojroot
BuildRequires : R-urltools
BuildRequires : R-webmockr
BuildRequires : R-yaml
BuildRequires : buildreq-R

%description
future runs. A port of the Ruby gem of the same name

%package lib
Summary: lib components for the R-vcr package.
Group: Libraries

%description lib
lib components for the R-vcr package.


%prep
%setup -q -c -n vcr
cd %{_builddir}/vcr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1621870764

%install
export SOURCE_DATE_EPOCH=1621870764
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
/usr/lib64/R/library/vcr/doc/cassette-manual-editing.R
/usr/lib64/R/library/vcr/doc/cassette-manual-editing.Rmd
/usr/lib64/R/library/vcr/doc/cassette-manual-editing.html
/usr/lib64/R/library/vcr/doc/configuration.R
/usr/lib64/R/library/vcr/doc/configuration.Rmd
/usr/lib64/R/library/vcr/doc/configuration.html
/usr/lib64/R/library/vcr/doc/debugging.R
/usr/lib64/R/library/vcr/doc/debugging.Rmd
/usr/lib64/R/library/vcr/doc/debugging.html
/usr/lib64/R/library/vcr/doc/design.R
/usr/lib64/R/library/vcr/doc/design.Rmd
/usr/lib64/R/library/vcr/doc/design.html
/usr/lib64/R/library/vcr/doc/index.html
/usr/lib64/R/library/vcr/doc/internals.R
/usr/lib64/R/library/vcr/doc/internals.Rmd
/usr/lib64/R/library/vcr/doc/internals.html
/usr/lib64/R/library/vcr/doc/lightswitch.R
/usr/lib64/R/library/vcr/doc/lightswitch.Rmd
/usr/lib64/R/library/vcr/doc/lightswitch.html
/usr/lib64/R/library/vcr/doc/record-modes.R
/usr/lib64/R/library/vcr/doc/record-modes.Rmd
/usr/lib64/R/library/vcr/doc/record-modes.html
/usr/lib64/R/library/vcr/doc/request_matching.R
/usr/lib64/R/library/vcr/doc/request_matching.Rmd
/usr/lib64/R/library/vcr/doc/request_matching.html
/usr/lib64/R/library/vcr/doc/vcr.R
/usr/lib64/R/library/vcr/doc/vcr.Rmd
/usr/lib64/R/library/vcr/doc/vcr.html
/usr/lib64/R/library/vcr/doc/write-to-disk.R
/usr/lib64/R/library/vcr/doc/write-to-disk.Rmd
/usr/lib64/R/library/vcr/doc/write-to-disk.html
/usr/lib64/R/library/vcr/help/AnIndex
/usr/lib64/R/library/vcr/help/aliases.rds
/usr/lib64/R/library/vcr/help/paths.rds
/usr/lib64/R/library/vcr/help/vcr.rdb
/usr/lib64/R/library/vcr/help/vcr.rdx
/usr/lib64/R/library/vcr/html/00Index.html
/usr/lib64/R/library/vcr/html/R.css
/usr/lib64/R/library/vcr/tests/test-all.R
/usr/lib64/R/library/vcr/tests/testthat/cassettes/ropenaq-encoding.yaml
/usr/lib64/R/library/vcr/tests/testthat/crul_resp1.rda
/usr/lib64/R/library/vcr/tests/testthat/crul_resp2.rda
/usr/lib64/R/library/vcr/tests/testthat/google_response.rda
/usr/lib64/R/library/vcr/tests/testthat/helper-vcr.R
/usr/lib64/R/library/vcr/tests/testthat/httr_obj.rda
/usr/lib64/R/library/vcr/tests/testthat/httr_resp1.rda
/usr/lib64/R/library/vcr/tests/testthat/httr_resp2.rda
/usr/lib64/R/library/vcr/tests/testthat/png_eg.rda
/usr/lib64/R/library/vcr/tests/testthat/test-Cassette.R
/usr/lib64/R/library/vcr/tests/testthat/test-Filesystem.R
/usr/lib64/R/library/vcr/tests/testthat/test-HttpInteraction.R
/usr/lib64/R/library/vcr/tests/testthat/test-HttpInteractionList.R
/usr/lib64/R/library/vcr/tests/testthat/test-Persisters.R
/usr/lib64/R/library/vcr/tests/testthat/test-Request.R
/usr/lib64/R/library/vcr/tests/testthat/test-RequestHandler.R
/usr/lib64/R/library/vcr/tests/testthat/test-RequestIgnorer.R
/usr/lib64/R/library/vcr/tests/testthat/test-RequestMatcherRegistry.R
/usr/lib64/R/library/vcr/tests/testthat/test-ause_cassette.R
/usr/lib64/R/library/vcr/tests/testthat/test-ause_cassette_match_body_empty_body.R
/usr/lib64/R/library/vcr/tests/testthat/test-ause_cassette_match_requests_on.R
/usr/lib64/R/library/vcr/tests/testthat/test-ause_cassette_match_requests_on_json.R
/usr/lib64/R/library/vcr/tests/testthat/test-ause_cassette_re_record.R
/usr/lib64/R/library/vcr/tests/testthat/test-ause_cassette_record_modes.R
/usr/lib64/R/library/vcr/tests/testthat/test-ause_cassette_write_to_disk.R
/usr/lib64/R/library/vcr/tests/testthat/test-ause_cassette_write_to_disk_binary_files.R
/usr/lib64/R/library/vcr/tests/testthat/test-binary_images.R
/usr/lib64/R/library/vcr/tests/testthat/test-cassette_options.R
/usr/lib64/R/library/vcr/tests/testthat/test-cassettes.R
/usr/lib64/R/library/vcr/tests/testthat/test-check_cassette_names.R
/usr/lib64/R/library/vcr/tests/testthat/test-configuration-inheritance.R
/usr/lib64/R/library/vcr/tests/testthat/test-configuration.R
/usr/lib64/R/library/vcr/tests/testthat/test-crul.R
/usr/lib64/R/library/vcr/tests/testthat/test-eject_cassette.R
/usr/lib64/R/library/vcr/tests/testthat/test-errors.R
/usr/lib64/R/library/vcr/tests/testthat/test-filter-sensitive-strings.R
/usr/lib64/R/library/vcr/tests/testthat/test-filter_headers.R
/usr/lib64/R/library/vcr/tests/testthat/test-filter_query_parameters.R
/usr/lib64/R/library/vcr/tests/testthat/test-httr.R
/usr/lib64/R/library/vcr/tests/testthat/test-insert_cassette.R
/usr/lib64/R/library/vcr/tests/testthat/test-lightswitch.R
/usr/lib64/R/library/vcr/tests/testthat/test-logger.R
/usr/lib64/R/library/vcr/tests/testthat/test-no-cassette-in-use.R
/usr/lib64/R/library/vcr/tests/testthat/test-quiet.R
/usr/lib64/R/library/vcr/tests/testthat/test-request_summary.R
/usr/lib64/R/library/vcr/tests/testthat/test-response_summary.R
/usr/lib64/R/library/vcr/tests/testthat/test-serializer.R
/usr/lib64/R/library/vcr/tests/testthat/test-serializers.R
/usr/lib64/R/library/vcr/tests/testthat/test-serializers_json.R
/usr/lib64/R/library/vcr/tests/testthat/test-serializers_yaml.R
/usr/lib64/R/library/vcr/tests/testthat/test-skip-vcr-off.R
/usr/lib64/R/library/vcr/tests/testthat/test-use_vcr.R
/usr/lib64/R/library/vcr/tests/testthat/test-utils.R
/usr/lib64/R/library/vcr/tests/testthat/test-vcr_last_error.R
/usr/lib64/R/library/vcr/tests/testthat/test-vcr_test_path.R
/usr/lib64/R/library/vcr/tests/testthat/test-write_disk_path_package_context.R
/usr/lib64/R/library/vcr/tests/testthat/test-write_interactions.R
/usr/lib64/R/library/vcr/tests/testthat/test-write_utils.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/vcr/libs/vcr.so
