#!/usr/bin/perl

use strict;

# parsing states 
my $g_open = 1;
my $g_label = 2;

sub log_dbg{
#    my ($msg) = @_;
#    print "DBG $msg\n";
}

sub log_err{
    my ($msg) = @_;
    print STDERR "ERROR $msg\n";
}

sub add_node{
    my ($level, $label, $content) = @_;
    for(my $i = 1; $i < $level; ++ $i){
        print STDOUT '| ';
    }
    print STDOUT "--$label";
    if(defined $content){
        print " $content\n";
    }
    else{
        print "\n";
    }
}


#( => OPEN
#( LABEL => LABEL
#
sub parse_line{
    my ($ref_ctx, $text) = @_;
    my $state = $$ref_ctx{'state'};
    my $level = $$ref_ctx{'level'};
    log_dbg("PARSE level={$level}, text={$text}");
    my $len = length($text);
    if($len == 0){
        return 0;
    }
    my $next_start = $len;
    do{
        my $label_closed = 0;
        my $label_end = $len;
        $len = length($text);
        $next_start = $len;
        log_dbg("DO PARSE state = {$state} level={$level}, text={$text}");
        if($state == $g_open){
            for(my $i = 0; $i < $len; ++ $i){
                my $char = substr($text, $i, 1);
                if($char eq ')'){
                    $label_closed = 1;
                    $label_end = $i - 1;
                    $next_start = $i + 1;
                    last;
                }
                elsif($char eq '('){
                    $label_end = $i - 1;
                    $next_start = $i;
                    last;
                }
            }
            if($label_end < 0){
                log_err("Bad text: $text");
                return -1;
            }
            if($label_end >= 0){
                my $node = substr($text, 0, $label_end + 1);
                my ($label, $content) = split /\s+/, $node;
                add_node($level, $label, $content);
                $state = $g_label;
            }
            if($label_closed == 1){
                -- $level;
            }
        }
        else{
            $next_start = $len;
            for(my $i = 0; $i < $len; ++ $i){
                my $char = substr($text, $i, 1);
                if($char eq '('){
                    ++ $level;
                    $state = $g_open;
                    $next_start = $i + 1;
                    last;
                }
            }
        }
        for(; $next_start < $len; ++ $next_start){
            if(substr($text, $next_start, 1) eq ')'){
                -- $level;
            }
            else{
                last;
            }
        }
        if($next_start < $len){
            $text = substr($text, $next_start);
        }
#        else{
#            last;
#        }
    }while($next_start < $len);
    $$ref_ctx{'state'} = $state;
    $$ref_ctx{'level'} = $level;
    return 0;
}
    
        
sub main{
    my %ctx = ( 'state' => $g_label,
                'level' => 0,
        );
    while(<>){
        chomp;
        parse_line(\%ctx, $_);
    }
#    print "\n----\nEND\n";
}

main();

