import { Upload, Button } from 'antd';
import { UploadOutlined } from '@ant-design/icons';
export default () => (
  // <Upload {...props}>
  //   <Button icon={<UploadOutlined />}>Click to Upload</Button>
  // </Upload>
  <Upload
  accept=".txt, .csv"
  showUploadList={false}
  beforeUpload={file => {
      const reader = new FileReader();

      reader.onload = e => {
          console.log(e.target.result);
      };
      reader.readAsText(file);

      // Prevent upload
      return false;
  }}
>
  <Button>
  <UploadOutlined type="upload" />
      {/* <Icon /> Click to Upload */}
  </Button>
</Upload>
);