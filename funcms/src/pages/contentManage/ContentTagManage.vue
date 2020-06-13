<template>
  <div>
    <content-tag-add ref="addDialog"></content-tag-add>
    <el-card shadow="never">
      <div slot="header">
        <span>分类标签管理</span>
      </div>
      <div>
        <div>
          <el-form :inline="true" :model="queryForm" class="demo-form-inline">
            <el-form-item label="内容类型">
              <el-select v-model="queryForm.contentType" placeholder="内容类型" value="0">
                <el-option label="空占位类型" value="0"></el-option>
                <el-option label="小说" value="1"></el-option>
                <el-option label="漫画" value="2"></el-option>
                <el-option label="动画" value="3"></el-option>
                <el-option label="游戏" value="4"></el-option>
                <el-option label="绘画图集" value="5"></el-option>
                <el-option label="素材资源" value="6"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="handleQuery">查询</el-button>
              <el-button type="default" @click="handleQueryReset">清空</el-button>
            </el-form-item>
            <el-form-item style="float: right;">
              <el-button type="primary" @click="handleAdd">添加</el-button>
            </el-form-item>
          </el-form>

        </div>
        <div>
          <el-table :data="contentTagTable.contentTagData" :border="true" v-loading="contentTagTable.loading">
            <el-table-column prop="contentType" label="内容类型" :width="150" :resizable="true"></el-table-column>
            <el-table-column prop="name" label="标签名" :width="200" :resizable="true"></el-table-column>
            <el-table-column prop="tagImageUrl" label="标签封面图片" :min-width="650" :resizable="true">
              <template slot-scope="scope">
                <el-popover placement="bottom" width="152" trigger="hover">
                  <img class="table-img" :src="scope.row.tagImageUrl"/>
                  <div slot="reference" class="name-wrapper">
                    <el-tag size="medium">{{ scope.row.tagImageUrl }}</el-tag>
                  </div>
                </el-popover>
              </template>
            </el-table-column>
            <el-table-column prop="operation" label="操作" fixed="right" :width="152">
              <template slot-scope="scope">
                <el-button
                    size="mini"
                    @click="handleEdit(scope.row)">编辑
                </el-button>
                <el-button
                    size="mini"
                    type="danger"
                    @click="handleDelete(scope.row)">删除
                </el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
  import axios from 'axios'
  import {getContentType, rspStatusHandler} from "../../consts"
  import ContentTagAdd from './ContentTagAdd'

  export default {
    name: "ContentTagManage",
    components: {ContentTagAdd},
    comments: {ContentTagAdd},
    data() {
      return {
        queryForm: {
          contentType: ''
        },
        contentTagTable: {
          loading: false,
          contentTagData: []
        }
      }
    },
    created() {
      this.reloadTable();
    },
    methods: {
      // 查询表单
      handleQuery() {
        this.reloadTable(this.queryForm.contentType);
      },
      handleQueryReset() {
        this.queryForm.contentType = '';
        this.handleQuery();
      },
      handleAdd() {
        this.$refs.addDialog.show('add');
      },
      // 表格操作
      reloadTable(contentType = null) {
        this.contentTagTable.loading = true;
        let params = {};
        if (contentType !== null && contentType !== '') {
          params.contentType = contentType;
        }
        axios
            .get('/backend/api/contentTags', {params})
            .then((resp) => {
              console.log(resp);
              this.contentTagTable.loading = false;
              let data = resp.data.data;
              this.contentTagTable.contentTagData = [];
              for (let d of data) {
                this.contentTagTable.contentTagData.push({
                  id: d.id,
                  contentType: getContentType(d.content_type),
                  name: d.name,
                  tagImageUrl: d.tag_img_url
                });
              }
            })
            .catch((err) => {
              console.error(err);
              this.loading = false;
              let status = err.response.status;
              this.$message.error(rspStatusHandler('NET', status));
              if (status === 403) {
                this.$router.push('/login');
              }
            });
      },
      handleEdit(row) {
        this.$refs.addDialog.show('update', row.id);
      },
      handleDelete(row) {
        let that = this;

        this.$confirm('此操作将删除所选内容标签, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.contentTagTable.loading = true;
          axios
              .delete('/backend/api/contentTags', {
                params: {id: row.id},
                headers: {'X-CSRFToken': that.$cookies.get('csrftoken')}
              })
              .then((resp) => {
                console.log(resp);
                this.contentTagTable.loading = false;
                let rsp = resp.data;
                if (rsp.rspCode !== '0') {
                  this.$message.error(rsp.rspMsg);
                } else {
                  this.$message.success('删除成功');
                  this.reloadTable();
                }
              })
              .catch((err) => {
                console.error(err);
                this.loading = false;
                let status = err.response.status;
                this.$message.error(rspStatusHandler('NET', status));
                if (status === 403) {
                  this.$router.push('/login');
                }
              });
        });
      }
    }
  }
</script>

<style scoped>
  .table-img {
    width: 150px;
    height: 200px;
  }
</style>