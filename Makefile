.PHONY: sync bundles check-bundles test build upload check clean

# test: the G1 CLI test — `sdlc-squad prompt` output == the canonical files in order.
test:
	python3 tests/cli/test_prompt.py

# bundles: generate usage/bundles/ (one paste per skill) from the canonical files.
# Generated artifacts, committed so pip users receive them; `make check-bundles`
# guards freshness.
bundles:
	scripts/build-bundles.sh

# check-bundles: fail if usage/bundles/ is stale vs the canonical files.
check-bundles:
	@tmp=$$(mktemp -d) && \
	 scripts/build-bundles.sh "$$tmp" >/dev/null && \
	 if diff -r usage/bundles "$$tmp" >/dev/null; then \
	   echo "bundles: fresh"; rm -rf "$$tmp"; \
	 else \
	   echo "bundles: STALE — run 'make bundles'"; diff -rq usage/bundles "$$tmp"; rm -rf "$$tmp"; exit 1; \
	 fi

# sync: generate the package copy of the kit (build artifact, gitignored —
# the repo root stays the single canonical copy; nothing is edited here)
# NOTE: no trailing slashes on the source dirs — rsync would flatten them.
sync:
	rsync -a --delete --exclude '.git/' \
		README.md WHAT-THIS-IS.md AGENTS.md CONVENTIONS.md ROADMAP.md CHANGELOG.md \
		CONTRIBUTING.md CODE_OF_CONDUCT.md SECURITY.md SUPPORT.md LICENSE \
		usage docs roles skills shared tests \
		sdlc_squad/kit/

# build: sync, then sdist + wheel
build: sync
	python3 -m build

# check: verify the wheel carries the kit before upload
check: build
	python3 -m twine check dist/sdlc_squad-$(shell python3 -c 'import sdlc_squad; print(sdlc_squad.__version__)')*

# upload: check, then publish to PyPI
upload: check
	python3 -m twine upload dist/sdlc_squad-$(shell python3 -c 'import sdlc_squad; print(sdlc_squad.__version__)')*

clean:
	rm -rf dist build *.egg-info sdlc_squad/kit