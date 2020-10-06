# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe


def get_context(context):
	path = frappe.request.path

	if path.startswith("/"):
		path = path[1:]

	if path.startswith("docs"):
		context.update(
			{
				"docs_search_scope": "docs",
				"docs_navbar_items": [
					{"label": "Facebook", "url": "https://www.facebook.com/ERPNextMN/"},
					{"label": "Twitter", "url": "https://twitter.com/ERPNextMNfrappetech"},
				],
			}
		)
