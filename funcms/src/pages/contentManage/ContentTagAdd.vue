<template>
  <el-dialog :title="title" :visible.sync="dialogVisible">
    <el-form ref="addForm" :model="addForm" :rules="rules" v-loading="loading" label-width="100px">
      <el-form-item label="内容类型" prop="contentType">
        <el-select v-model="addForm.contentType" placeholder="内容类型" value="0">
          <el-option label="空占位类型" value="0"></el-option>
          <el-option label="小说" :value="1"></el-option>
          <el-option label="漫画" :value="2"></el-option>
          <el-option label="动画" :value="3"></el-option>
          <el-option label="游戏" :value="4"></el-option>
          <el-option label="绘画图集" :value="5"></el-option>
          <el-option label="素材资源" :value="6"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="标签名" prop="name">
        <el-input v-model="addForm.name" auto-complete="off" class="dialog-input"></el-input>
      </el-form-item>
      <el-form-item label="封面图片" prop="tagImageUrl">
        <el-tooltip class="item" effect="dark" content="推荐图片尺寸在150px*200px" placement="bottom">
          <el-input v-model="addForm.tagImageUrl" auto-complete="off" class="dialog-input"></el-input>
        </el-tooltip>
      </el-form-item>
    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button @click="onCancel">取消</el-button>
      <el-button type="primary" @click="onConfirm">确定</el-button>
    </div>
  </el-dialog>
</template>

<script>
  import request from '../../utils/request';

  export default {
    name: "ContentTagAdd",
    data() {
      return {
        dialogVisible: false,
        loading: false,
        title: '',
        updateMode: 'add',
        addForm: {
          id: '',
          contentType: '',
          name: '',
          tagImageUrl: ''
        },
        rules: {
          contentType: [
            {required: true, message: '请选择内容类型', trigger: 'blur'}
          ],
          name: [
            {required: true, message: '请输入标签名', trigger: 'blur'},
            {max: 255, message: '标签名不能超过255个字符', trigger: 'blur'},
          ],
          tagImageUrl: [
            {required: true, message: '请输入标签图片', trigger: 'blur'},
            {max: 255, message: '标签图片不能超过255个字符', trigger: 'blur'},
          ],
        },
      }
    },
    methods: {
      show(updateMode, idx) {
        this.dialogVisible = true;
        this.resetFormData();
        this.$nextTick(function () {
          this.$refs.addForm.resetFields();
        });
        if (updateMode === 'update') {
          this.title = '更新内容标签';
          this.updateMode = 'update';
          this.loading = true;

          request.get('/backend/api/contentTags/' + idx, {
            success: (resp) => {
              this.loading = false;
              let rsp = resp.data;
              if (rsp.rspCode !== '0') {
                this.$message.error(rsp.rspMsg);
              } else {
                this.addForm.id = rsp.data['id'];
                this.addForm.contentType = rsp.data['content_type'];
                this.addForm.name = rsp.data['name'];
                this.addForm.tagImageUrl = rsp.data['tag_img_url'];
              }
            },
            failure: () => {
              this.loading = false;
            }
          });
        } else {
          this.title = '添加内容标签';
          this.updateMode = 'add';
        }
      },
      hide() {
        this.dialogVisible = false;
      },
      resetFormData() {
        this.addForm = {
          id: '',
          contentType: '',
          name: '',
          tagImageUrl: ''
        };
      },
      onCancel() {
        this.hide();
      },
      onConfirm() {
        let that = this;
        this.$refs.addForm.validate((valid) => {
          if (valid) {
            this.loading = true;
            if (this.updateMode === 'update') {

              request.put('/backend/api/contentTags/' + this.addForm.id, {
                headers: {'X-CSRFToken': that.$cookies.get('csrftoken')},
                data: this.addForm,
                success: (resp) => {
                  this.loading = false;
                  let rsp = resp.data;
                  if (rsp.rspCode !== '0') {
                    this.$message.error(rsp.rspMsg);
                  } else {
                    this.$message.success('更新成功');
                    this.hide();
                    this.$parent.handleQueryReset();
                  }
                },
                failure: () => {
                  this.loading = false;
                }

              });
            } else {

              request.post('/backend/api/contentTags', {
                data: this.addForm,
                headers: {'X-CSRFToken': that.$cookies.get('csrftoken')},
                success: (resp) => {
                  this.loading = false;
                  let rsp = resp.data;
                  if (rsp.rspCode !== '0') {
                    this.$message.error(rsp.rspMsg);
                  } else {
                    this.$message.success('添加成功');
                    this.hide();
                    this.$parent.handleQueryReset();
                  }
                },
                failure: () => {
                  this.loading = false;
                }
              });
            }
          }
        });
      }
    }
  }
</script>

<style scoped>

</style>