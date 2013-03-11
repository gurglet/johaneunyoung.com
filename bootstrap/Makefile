BUILD_DIR = build/
DESTDIR = ../wedding/templates/
LESS_COMPRESSOR = node less.js/bin/lessc
LESS_FLAGS = -sm -su
SRC_FILES = twitter-bootstrap/less/*.less *.less

bootstrap:
	mkdir -p $(BUILD_DIR)
	cp $(SRC_FILES) $(BUILD_DIR)
	echo '@import "responsive.less";' >> build/bootstrap.less
	echo '@import "bootswatch.less";' >> build/bootstrap.less
	$(LESS_COMPRESSOR) $(LESS_FLAGS) $(BUILD_DIR)bootstrap.less > $(DESTDIR)bootstrap.css
