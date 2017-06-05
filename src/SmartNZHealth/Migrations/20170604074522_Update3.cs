using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore.Migrations;

namespace SmartNZHealth.Migrations
{
    public partial class Update3 : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Cases_AspNetUsers_ApplicationUserId",
                table: "Cases");

            migrationBuilder.DropIndex(
                name: "IX_Cases_ApplicationUserId",
                table: "Cases");

            migrationBuilder.DropColumn(
                name: "ApplicationUserId",
                table: "Cases");

            migrationBuilder.AddColumn<string>(
                name: "DoctorId",
                table: "Cases",
                nullable: true);

            migrationBuilder.AddColumn<string>(
                name: "PatientId",
                table: "Cases",
                nullable: true);

            migrationBuilder.CreateIndex(
                name: "IX_Cases_PatientId",
                table: "Cases",
                column: "PatientId");

            migrationBuilder.AddForeignKey(
                name: "FK_Cases_AspNetUsers_PatientId",
                table: "Cases",
                column: "PatientId",
                principalTable: "AspNetUsers",
                principalColumn: "Id",
                onDelete: ReferentialAction.Restrict);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Cases_AspNetUsers_PatientId",
                table: "Cases");

            migrationBuilder.DropIndex(
                name: "IX_Cases_PatientId",
                table: "Cases");

            migrationBuilder.DropColumn(
                name: "DoctorId",
                table: "Cases");

            migrationBuilder.DropColumn(
                name: "PatientId",
                table: "Cases");

            migrationBuilder.AddColumn<string>(
                name: "ApplicationUserId",
                table: "Cases",
                nullable: true);

            migrationBuilder.CreateIndex(
                name: "IX_Cases_ApplicationUserId",
                table: "Cases",
                column: "ApplicationUserId");

            migrationBuilder.AddForeignKey(
                name: "FK_Cases_AspNetUsers_ApplicationUserId",
                table: "Cases",
                column: "ApplicationUserId",
                principalTable: "AspNetUsers",
                principalColumn: "Id",
                onDelete: ReferentialAction.Restrict);
        }
    }
}
