from ohapi import api
import tempfile
import os


def upload_notebook(notebook_content,
                    notebook_name,
                    access_token,
                    project_member_id):
    """
    Upload a notebook to the Personal Data Notebook project on Open Humans.
    """
    tmp_directory = tempfile.mkdtemp()
    metadata = {
        'description': 'A Personal Data Notebook',
        'tags': ['personal data notebook', 'notebook', 'jupyter']
    }
    out_file = os.path.join(tmp_directory, notebook_name)
    with open(out_file, 'wb') as tmp_notebook:
        tmp_notebook.write(notebook_content)
        tmp_notebook.flush()
    print(out_file)
    upload_response = api.upload_aws(out_file,
                                     metadata,
                                     access_token,
                                     project_member_id=project_member_id)
    return upload_response
