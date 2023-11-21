from flask import Flask, jsonify
from google.cloud import storage

app = Flask(__name__)

# Replace 'your-project-id' and 'your-bucket-name' with your actual project ID and bucket name
project_id = 'prj-futurae-d51c'
bucket_name = 'prj-futurae-d51c-futurae-bucket'

# Initialize the GCS client
storage_client = storage.Client(project=project_id)
bucket = storage_client.get_bucket(bucket_name)


@app.route('/list_all', methods=['GET'])
def list_all_objects():
    try:
        # List all objects in the bucket
        objects = bucket.list_blobs()

        # Extract object names
        object_names = [obj.name for obj in objects]

        return jsonify({'objects': object_names})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
