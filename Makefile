.PHONY: push-langs
push-langs:
	git pull
	git add --all
	git commit -m "Update translations"
	git push
